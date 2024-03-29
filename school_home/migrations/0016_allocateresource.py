# Generated by Django 2.2.3 on 2019-07-28 04:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school_home', '0015_auto_20190728_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllocateResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('year', models.DateField(default=django.utils.timezone.now)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_home.Resource')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_home.School')),
            ],
        ),
    ]
