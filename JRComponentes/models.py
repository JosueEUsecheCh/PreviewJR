from django.db import models

# Create your models here.

class categoriaComponentes(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='categoriaComponente'
        verbose_name_plural='categoriaComponentes'
    def __str__(self):
        return self.name


class Componentes(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='Componentes')
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0.00)
    category= models.ForeignKey(categoriaComponentes, on_delete=models.CASCADE)
    avaiability= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Componente'
        verbose_name_plural='Componentes'
    def __str__(self):
        return self.name

