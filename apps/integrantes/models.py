from django.db import models

# Create your models here.



class Integrantes(models.Model):
    NIVEL = (
        ('1-PRE', 'Presidente'),
        ('3-VIC', 'Vice-Presidente'),
        ('5-DIR', 'Diretor'),
        ('2-INT', 'Integrante'),
        ('4-PRO', 'Prospero'),
        ('6-ESP', 'Espelho')
    )

    nome_integrante = models.CharField(max_length=100)
    foto_integrante = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    data_entrada = models.DateTimeField()
    integrante_ativo = models.BooleanField(default=True)
    cargo_integrante = models.CharField(max_length=5, choices=NIVEL, blank=False, null=False, default='4-INT')

    def __str__(self):
        return self.nome_integrante


class InMemorian(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
