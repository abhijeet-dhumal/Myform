# Generated by Django 3.2.8 on 2022-02-03 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('role', models.CharField(blank=True, default='Patient', max_length=50, verbose_name='Role')),
                ('phone', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/patient/')),
                ('address_line1', models.CharField(blank=True, max_length=100, verbose_name='Address_Line1')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=50, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Country')),
                ('pincode', models.CharField(blank=True, max_length=50, verbose_name='Pincode')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('role', models.CharField(blank=True, default='Doctor', max_length=50, verbose_name='Role')),
                ('phone', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/doctor/')),
                ('address_line1', models.CharField(blank=True, max_length=100, verbose_name='Address_Line1')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=50, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Country')),
                ('pincode', models.CharField(blank=True, max_length=50, verbose_name='Pincode')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]