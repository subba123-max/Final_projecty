# Generated by Django 2.2.13 on 2021-01-04 05:31

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
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('created_At', models.DateField(auto_now_add=True)),
                ('updated_At', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=20)),
                ('mode_of_payment', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to=None)),
                ('price', models.IntegerField()),
                ('created_At', models.DateField(auto_now_add=True)),
                ('updated_At', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingCart.Orders')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingCart.Products')),
            ],
        ),
    ]
