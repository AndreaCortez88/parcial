from django.db import models

# Create your models here.

class Empleado(models.Model):
    pk_empleado = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=False, blank=False)
    usuario = models.CharField(max_length=20, null=False, blank=False)
    contraseña = models.CharField(max_length=8, null=False, blank=False)

    class Meta:
        verbose_name='empleado'
        verbose_name_plural='empleados'
        ordering=['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)


class ordenador(models.Model):
    pk_ordenador = models.AutoField(primary_key=True, null=False, blank=False)
    nombre_ordenador = models.CharField(max_length=9, null=False, blank=False)
    num_ordenador = models.CharField(max_length=9, null=False, blank=False)
    imagen1 = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)


    class Meta:
        verbose_name='ordenador'
        verbose_name_plural='ordenadores'
        ordering=['nombre_ordenador']

    def __str__(self):
        return "{0}".format(self.nombre_ordenador)