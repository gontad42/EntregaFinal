# Generated by Django 4.0.3 on 2022-04-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('autor', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=20)),
                ('editorial', models.CharField(max_length=50)),
                ('año', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('titulo', models.CharField(max_length=40)),
                ('fecha_prest', models.DateField()),
            ],
        ),
    ]