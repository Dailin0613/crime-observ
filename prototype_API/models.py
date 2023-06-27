from django.db import models


class Persona(models.Model):
    FEMENINO = 'F'
    MASCULINO = 'M'

    GENERO_CHOICE = [
        (FEMENINO, 'Femenino'),
        (MASCULINO, 'Masculino')
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICE)
    direccion = models.CharField(max_length=200)
    ocupacion = models.CharField(max_length=255)
    descripcion_fisica = models.TextField()

    class Meta:
        abstract = True


class Delincuente(Persona):
    situacion_economica = models.TextField()
    situacion_social = models.TextField()


class Victima(Persona):
    pass


class Oficial(Persona):
    rango = models.CharField(max_length=200)


class Testigo(Persona):
    pass


class Sospechoso(Persona):
    pass


class TipoDelito(models.Model):
    nombre = models.CharField(max_length=200)


class Delito(models.Model):
    fecha = models.DateField()
    hora = models.DateTimeField()
    ubicacion = models.CharField(max_length=100)
    da_materiales = models.TextField()
    tipo_delito = models.ForeignKey(TipoDelito, on_delete=models.CASCADE)
    # foreign_key
    delincuente = models.ForeignKey(Delincuente, on_delete=models.CASCADE)
    victima = models.ForeignKey(Victima, on_delete=models.CASCADE)
    sospechoso = models.ForeignKey(Sospechoso, on_delete=models.CASCADE)
    testigo = models.ForeignKey(Testigo, on_delete=models.CASCADE)
    oficial = models.ForeignKey(Oficial, on_delete=models.CASCADE)


class Pruebas(models.Model):
    prueba = models.BigAutoField(primary_key=True, auto_created=True)
    delito = models.ManyToManyField(Delito, through='PruebasDelito', through_fields=('prueba', 'delito'))


class PruebasDelito(models.Model):
    tipo = models.CharField(max_length=100)
    resultado = models.TextField()
    fecha_prueba = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    delito = models.ForeignKey(Delito, on_delete=models.CASCADE)
    prueba = models.ForeignKey(Pruebas, on_delete=models.CASCADE)
