from django.db import models
from bases.models import BaseModel
from django.urls import reverse


class Brand(BaseModel):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class CarModel(BaseModel):
    description = models.CharField(
        max_length=50, db_comment="Car model description", verbose_name="Modelo"
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="Marca")

    def __str__(self):
        return f"{self.brand} - {self.description}"

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        permissions = [("read_write_permission", "Can read and write car models")]


class Vehicle(BaseModel):
    car_model = models.ForeignKey(
        CarModel, on_delete=models.RESTRICT, verbose_name="Modelo"
    )
    registration = models.CharField(
        max_length=20, help_text="Matricula", verbose_name="Matrícula"
    )
    year = models.PositiveSmallIntegerField(
        help_text="Año del modelo del vehículo", verbose_name="Año"
    )

    def __str__(self):
        return self.registration

    def get_absolute_url(self):
        return reverse("vehicle_edit", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        db_table_comment = "Vehículos"
