# Generated by Django 3.2 on 2021-04-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('cislo_rp', models.IntegerField()),
                ('datum_narozeni', models.DateField()),
            ],
        ),
    ]
