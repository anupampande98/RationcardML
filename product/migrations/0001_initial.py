# Generated by Django 3.0.3 on 2021-03-16 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.ImageField(upload_to=product.models.upload_file_path)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('apl_price', models.DecimalField(decimal_places=2, default=5.0, max_digits=20)),
                ('apl_limit', models.IntegerField(default=5)),
                ('bpl_price', models.DecimalField(decimal_places=2, default=5.0, max_digits=20)),
                ('bpl_limit', models.IntegerField(default=5)),
                ('aay_price', models.DecimalField(decimal_places=2, default=5.0, max_digits=20)),
                ('aay_limit', models.IntegerField(default=5)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Family')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.Distributor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product')),
            ],
            options={
                'unique_together': {('product', 'distributor')},
            },
        ),
        migrations.CreateModel(
            name='NextDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None, validators=[product.models.validate_date])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.Distributor')),
            ],
            options={
                'unique_together': {('date', 'distributor')},
            },
        ),
    ]
