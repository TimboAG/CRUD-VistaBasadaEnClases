# Generated by Django 4.2.1 on 2023-05-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_autor_options_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
    ]
