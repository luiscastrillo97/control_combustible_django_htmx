# Generated by Django 4.2.9 on 2024-02-27 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ctrl_comb', '0004_brand_created_at_brand_created_by_brand_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('registration', models.CharField(help_text='Matricula', max_length=20)),
                ('year', models.PositiveSmallIntegerField(help_text='Año del modelo del vehículo')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ctrl_comb.carmodel')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vehículo',
                'verbose_name_plural': 'Vehículos',
                'db_table_comment': 'Vehículos',
            },
        ),
    ]