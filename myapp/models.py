from django.db import models
from datetime import datetime


# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return "{} - {}".format(self.nmae, self.email)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-id']

# opções de Imoveis
class TypeInmobile(models.TextChoices):
    APARTAMENTO = 'APARTAMENTO', 'APARTAMENTO'
    KITNET = 'KITNET', 'KITNET'
    HOUSE = 'CASA', 'CASA'

# cadastro de imoveis
class Inmobile(models.Model):
    code = models.CharField(max_length=100)
    type_item = models.CharField(max_length=100, choices=TypeInmobile.choices)
    address = models.TextField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    is_locate = models.BooleanField(default=False)
     

    def __str__(self):
        return "{} - {}".format(self.code, self.type_item)

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "imóveis"
        ordering = ['-id']

# cadastrar imagens

class InmobileImage(models.Model):
    image = models.ImageField('Images',upload_to='images')
    inmobile = models.ForeignKey(Inmobile, related_name='inmobile_images', on_delete=models.CASCADE)

    def __str__(self):
        return self.inmobile.code
    
# registrar locação
class RegisterLocations(models.Model):
    inmobile = models.ForeignKey(Inmobile, on_delete=models.CASCADE, related_name='reg_locacao')
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dt_start = models.DateTimeField('Início')
    dt_end = models.DateTimeField('Fim')
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "{} - {}".format(self.client, self.inmobile)
    
    class Meta:
        verbose_name = 'Registrar Locação'
        verbose_name_plural = 'Registrar Locação'
        ordering = ['-id']