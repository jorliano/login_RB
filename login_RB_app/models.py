from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=256,unique=True)


    def popularCategorias(self):
        self.name = 'cliente'
        self.save()
        self.name = 'concentrador'
        self.save()
        self.name = 'core'
        self.save()

    def __str__(self):
        return self.name

class Mikrotik(models.Model):
    name = models.CharField(max_length=264,unique=True)
    login = models.CharField(max_length=264, default='admin')
    password = models.CharField(max_length=50, blank=True)
    ip = models.CharField(max_length=15, default='192.168.0.88')
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
