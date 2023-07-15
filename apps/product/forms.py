from django import forms
from apps.product.models import Product, Banner, Rate
from ckeditor.widgets import CKEditorWidget


class BannerFrom(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Banner
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = "__all__"
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name.title()
