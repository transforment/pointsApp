# Generated by Django 4.1.3 on 2022-12-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogurt', '0007_remove_checkindata_coupon_alter_checkindata_idcus'),
    ]

    operations = [
        migrations.AddField(
            model_name='cusdata',
            name='provider',
            field=models.CharField(default='', max_length=200),
        ),
    ]
