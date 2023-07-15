from django.db import transaction
from import_export import resources
from .models import ProductImage


class ProductImageResource(resources.ModelResource):
    class Meta:
        model = ProductImage
        fields = ('id', 'product__title', 'color__title', 'price')

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        """
        Override to add additional logic. Does nothing by default.
        Manually removing commit hooks for intermediate savepoints of atomic transaction
        """
        for data in dataset:
            model = ProductImage.objects.get(id=data[0])
            model.price = data[1]
            model.save()
