# Generated by Django 4.1.3 on 2022-12-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogurt', '0003_alter_cusdata_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cusdata',
            name='last_check_in',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
