from django.db import models

# Create your models here.

class Populares(models.Model):

    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='Populares')

    class Meta:
        verbose_name='Populares'
        verbose_name_plural='Popular'
    def __str__(self):
        return self.name
