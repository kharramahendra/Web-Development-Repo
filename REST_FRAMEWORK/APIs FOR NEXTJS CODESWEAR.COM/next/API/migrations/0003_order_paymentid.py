# Generated by Django 4.1 on 2022-08-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_forgot_order_product_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymentid',
            field=models.CharField(default='', max_length=200),
        ),
    ]
