from django.db import models


class Encuestas(models.Model):
    ENCUESTA_CUALITATIVA = 'Cualitativa'
    ENCUESTA_CUANTITATIVA = 'Cuantitativa'
    TIPO_ENCUESTA = [
        (ENCUESTA_CUALITATIVA, 'Cualitativa'),
        (ENCUESTA_CUANTITATIVA, 'Cuantitativa')
    ]
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fecha_terminada = models.DateTimeField()
    tipo_encuesta = models.CharField(choices=TIPO_ENCUESTA, max_length=12)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class ContenidoEncuesta(models.Model):
    contenido = models.TextField()
    encuesta = models.ForeignKey(Encuestas, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido

    class Meta:
        abstract = True


class Preguntas(ContenidoEncuesta):
    pass


class Respuestas(ContenidoEncuesta):
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE, default=1)


class Analisis(models.Model):
    encuesta = models.ForeignKey(Encuestas, on_delete=models.CASCADE)
    analisis = models.URLField(unique=True)
    creado = models.DateTimeField(auto_now=True)
    actualizado = models.DateTimeField(auto_now_add=True)
