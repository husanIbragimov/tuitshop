from django.db import models


class BaseAbstractDate(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Variant(BaseAbstractDate):
    duration = models.IntegerField()
    percent = models.IntegerField()

    def __str__(self):
        return str(self.duration)
