# Generated by Django 4.2.9 on 2024-02-26 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctrl_comb', '0002_carmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'permissions': [('read_write_permission', 'Can read and write car models')], 'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ctrl_comb.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='description',
            field=models.CharField(db_comment='Car model description', max_length=50, verbose_name='Modelo'),
        ),
    ]
