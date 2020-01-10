# Generated by Django 2.2.2 on 2019-12-11 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personalidad', models.CharField(choices=[('ME', 'Muy extrovertido'), ('E', 'Extrovertido'), ('N', 'Neutral'), ('I', 'Introvertido'), ('MI', 'Muy introvertido')], max_length=2)),
                ('cant_ninos', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', 'Más de 5')], max_length=1)),
                ('edad', models.IntegerField()),
                ('deportes', models.CharField(choices=[('0', 'Ningún día'), ('1', 'Un día'), ('2', 'Dos días'), ('3', 'Tres días'), ('4', 'Cuatro días'), ('5', 'Cinco días'), ('6', 'Seis días'), ('7', 'Siete días')], max_length=2)),
                ('vivienda', models.CharField(choices=[('C', 'Casa con patio'), ('DC', 'Dpto Chico o Mediano'), ('DG', 'Dpto Grande'), ('P', 'Parcela')], max_length=2)),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.Mascota')),
            ],
        ),
    ]
