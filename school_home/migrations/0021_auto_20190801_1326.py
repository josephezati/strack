# Generated by Django 2.2.3 on 2019-08-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_home', '0020_deo_transferdeo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferdeo',
            name='date_valid',
            field=models.DateField(blank=True, null=True, verbose_name='Transfer Deo Until'),
        ),
    ]
