# Generated by Django 3.2.9 on 2022-01-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investissement',
            name='annee_d_individualisation',
            field=models.CharField(max_length=200, null=True, verbose_name='annee_d_indivi'),
        ),
    ]
