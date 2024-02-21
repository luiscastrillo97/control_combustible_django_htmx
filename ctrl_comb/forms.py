from django import forms
from .models import *


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({"class": "form-control"})
