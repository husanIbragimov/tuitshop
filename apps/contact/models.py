from django.db import models

from apps.base.models import BaseAbstractDate


class GetInTouch(BaseAbstractDate):
    STATUS = (
        (0, 'NEW'),
        (1, 'CANCELED'),
        (2, 'FINISHED'),
    )
    status = models.IntegerField(choices=STATUS, default=0)
    first_name = models.CharField(max_length=223, null=True, blank=True)
    last_name = models.CharField(max_length=223, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.first_name:
            return self.first_name
        return f'No name'


class Location(BaseAbstractDate):
    name = models.CharField(max_length=223, null=True, blank=True)
    address = models.CharField(max_length=223, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    location = models.URLField(null=True, blank=True)

    def __str__(self):
        if self.address:
            return self.address
        return f'No address'


class Subscribe(BaseAbstractDate):
    email = models.EmailField(null=True)

    def __str__(self):
        return f'{self.id}'
