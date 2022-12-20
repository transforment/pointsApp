# Generated by Django 4.1.3 on 2022-12-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CusData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('dateOfbirth', models.CharField(max_length=200)),
                ('point', models.IntegerField(default=0)),
                ('coupon', models.IntegerField(default=0)),
            ],
        ),
    ]