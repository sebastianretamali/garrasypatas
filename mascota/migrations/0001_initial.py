# Generated by Django 2.2.2 on 2019-10-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('raza', models.CharField(max_length=15)),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1)),
                ('tipo', models.CharField(choices=[('G', 'Gato'), ('P', 'Perro')], max_length=1)),
                ('estado', models.CharField(choices=[('A', 'Adulto'), ('C', 'Cachorrro')], max_length=1)),
                ('tamano', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='imgp/')),
                ('descripcion', models.TextField(max_length=100)),
            ],
        ),
    ]