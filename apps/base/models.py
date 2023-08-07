from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


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


class UserType(BaseAbstractDate):
    Role = (
        ("O'qtuvchi", "O'qtuvchi"),
        ('Talaba', 'talaba'),
        ("Buxg'alter", "Buxg'alter"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='role', null=True)
    role = models.CharField(max_length=50, choices=Role, default='Talaba', null=True, blank=True)

    def __str__(self):
        return f'{self.user}-{self.role}'


class Resume(BaseAbstractDate):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='profile', null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    birth_of_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    description = models.TextField(null=True, blank=False)
    specialist = models.CharField(max_length=255, null=True, blank=False)
    github = models.URLField(null=True, blank=False)
    linkedin = models.URLField(null=True, blank=False)
    telegram = models.URLField(null=True, blank=False)
    link_job = models.URLField(null=True, blank=False)
    cv = models.FileField(upload_to='pdf/cv', blank=True)

    def __str__(self):
        return str(self.user)

    def full_name(self):
        return f'{self.last_name} {self.first_name}'
