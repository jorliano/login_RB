from django.db import models
from django.core.validators import ip_address_validators
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class Categoria(models.Model):
    descricao = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.descricao

class Mikrotik(models.Model):
    descricao = models.CharField(max_length=264,unique=True)
    login = models.CharField(max_length=264, default='admin')
    senha = models.CharField(max_length=50, blank=True)
    ip = models.GenericIPAddressField(max_length=15, default='192.168.0.88',protocol='IPv4')
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

    # def save(self, *args, **kwargs):
    #     self.senha = make_password(self.senha)
    #     super(Mikrotik, self).save(*args, **kwargs)
