# Generated by Django 2.2.3 on 2019-07-28 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_home', '0016_allocateresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocateresource',
            name='date_allocated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='allocateresource',
            name='date_valid',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='allocateresource',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resource',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]