from django.db import models

# Create your models here.
class Usuario(models.Model):
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    nome = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome

class Pet(models.Model):


    TIPO_CHOICES = (
        ("Cachorro", "Cachorro"),
        ("Gato", "Gato"),
    )

    raca = models.CharField(max_length=50, null=False)
    cor = models.CharField(max_length=20, null=False)
    Quando_Foi_Encontrado = models.DateField(null=False,)
    Lugar_Onde_Foi_Achado = models.CharField(max_length=35, null=False)
    foto_capa = models.ImageField(upload_to='images')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    Usuario = models.ForeignKey(Usuario)


    def __str__(self):
        return self.raca
