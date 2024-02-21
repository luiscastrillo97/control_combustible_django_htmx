from django.db import models


class Brand(models.Model):
    description = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.description
