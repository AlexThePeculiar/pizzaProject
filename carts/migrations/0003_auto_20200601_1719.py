# Generated by Django 3.0.5 on 2020-06-01 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20200601_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='carts.Cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_total',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
