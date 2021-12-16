# Generated by Django 4.0 on 2021-12-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='supplier',
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.ManyToManyField(blank=True, null=True, to='inventory.Supplier'),
        ),
    ]