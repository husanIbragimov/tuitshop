from django import forms
from .models import GetInTouch, Subscribe


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ('first_name', 'last_name', 'phone_number', 'message')

    def __init__(self, *args, **kwargs):
        super(GetInTouchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name.title()
