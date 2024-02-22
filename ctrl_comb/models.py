from django.db import models


class Brand(models.Model):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class CarModel(models.Model):
    description = models.CharField(
        max_length=50, db_comment="Car model description", verbose_name="Modelo"
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="Marca")

    def __str__(self):
        return f"{self.brand} - {self.description}"

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
