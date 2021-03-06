# Generated by Django 3.2.8 on 2021-10-06 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('pk_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=8)),
                ('usuario', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ordenador',
            fields=[
                ('pk_ordenador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ordenador', models.CharField(max_length=9)),
                ('num_ordenador', models.CharField(max_length=9)),
                ('imagen1', models.URLField(default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', max_length=800)),
            ],
            options={
                'verbose_name': 'ordenador',
                'verbose_name_plural': 'ordenadores',
                'ordering': ['nombre_ordenador'],
            },
        ),
    ]
