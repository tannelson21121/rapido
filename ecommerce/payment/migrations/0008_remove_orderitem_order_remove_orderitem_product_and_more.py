# Generated by Django 4.1.2 on 2022-10-30 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_remove_order_products_ordered_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
