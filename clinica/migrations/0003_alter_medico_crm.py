# Generated by Django 4.2 on 2025-04-04 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_rename_consulta_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
