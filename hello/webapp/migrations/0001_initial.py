# Generated by Django 3.2 on 2021-04-30 13:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='описание')),
                ('remainder', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='remainder')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='webapp.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
    ]
