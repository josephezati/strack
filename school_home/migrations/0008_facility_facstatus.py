# Generated by Django 2.2.3 on 2019-07-23 20:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school_home', '0007_auto_20190723_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_status', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=45)),
                ('photo', models.ImageField(default='default.png', upload_to='fac_uploads')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('facility_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_home.FacType')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_home.School')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_home.FacStatus')),
            ],
        ),
    ]
