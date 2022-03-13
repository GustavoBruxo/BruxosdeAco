from django.db import models

# Create your models here.


class Album(models.Model):
    nome_album = models.CharField(max_length=100)
    foto_capa_album = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    local_album = models.CharField(max_length=100)
    data_album = models.DateTimeField()
    exibir_album = models.BooleanField(default=True)
    album_destaque = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_album


class Imagens(models.Model):
    id_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='album/%m/%Y/', blank=True)
