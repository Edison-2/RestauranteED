from django.db import models

# Create your models here.

class Provincia(models.Model):
    id_ed=models.AutoField(primary_key=True)
    region_ed = models.CharField(max_length=255)
    nombre_ed = models.CharField(max_length=255)
    capital_ed = models.CharField(max_length=255)
    prefijo_ed= models.CharField(max_length=225, null=True,blank=True)


    def __str__(self):
        fila="{0};{1} {2}"
        return fila.format(self.region_ed, self.nombre_ed, self.capital_ed )

class Cliente(models.Model):
    id_ed=models.AutoField(primary_key=True)
    nombre_ed = models.CharField(max_length=255)
    cedula_ed = models.CharField(max_length=15)
    correo_ed = models.EmailField()
    telefono_ed = models.CharField(max_length=15)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    def __str__(self):
        fila="{0};{1} {2}"
        return fila.format(self.nombre_ed, self.cedula_ed, self.correo_ed )
