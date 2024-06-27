from django.db import models

class CategoriaAudioVideo(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoría de Audio y Video'
        verbose_name_plural = 'Categorías de Audio y Video'

    def __str__(self):
        return self.name

class ComponenteAudioVideo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='AudioVideo')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(CategoriaAudioVideo, on_delete=models.CASCADE)
    avaiability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Componente de Audio y Video'
        verbose_name_plural = 'Componentes de Audio y Video'

    def __str__(self):
        return self.name
