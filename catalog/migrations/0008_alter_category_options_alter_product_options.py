# Generated by Django 5.0.6 on 2024-09-21 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_created_at_alter_product_updated_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name",),
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
