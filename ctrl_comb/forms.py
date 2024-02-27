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


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ["brand", "description"]


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["car_model", "registration", "year"]
