from django import forms
from JRComponentes.models import categoriaComponentes  
from JRAudio_video.models import CategoriaAudioVideo
from JREquipos.models import CategoriaEquipos 

class register_products(forms.Form):
    name = forms.CharField(label='Producto',
        max_length=100,
        required=True,
        help_text='Introduce el nombre del producto (máximo 100 caracteres).',
        error_messages={
            'required': 'Este campo es obligatorio.',
            'max_length': 'El nombre no puede exceder de 100 caracteres.'
        },
        widget=forms.TextInput(attrs={'class': 'custom-class', 'placeholder': 'Nombre del producto'}))    
    description = forms.CharField(label='Descripcion',max_length=500, required=False)
    image = forms.ImageField(required=True,
        label='Imagen',
        error_messages={
            'invalid': 'Solo se permiten archivos de imagen.',
            'required': 'Este campo es obligatorio.',
        },
        widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}))
    price = forms.DecimalField(max_digits=10,decimal_places=2,initial=0.00,label='precio', required=True,
                               widget=forms.NumberInput(attrs={
            'class': 'custom-class',  # Clase CSS personalizada.
            'placeholder': '0.00',  # Placeholder para el campo.
            'step': '0.01',  # Controla la precisión.
            'min': '0',  # Valor mínimo permitido.
            'max': '99999999.99'  # Valor máximo permitido acorde a max_digits.
        }))
    avaiability = forms.BooleanField(
        label='Disponibilidad',
        initial=True,  
        required=True,
        help_text='Marque esta casilla si el producto está disponible.',
        error_messages={
            'required': 'Debe marcar esta casilla para continuar.',
        },
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-checkbox',  # Clase CSS personalizada.
        }))
    category = forms.ChoiceField(
        choices=[],  # Las opciones se llenarán dinámicamente más adelante
        label='Categoría',
        required=True,
        widget=forms.Select(attrs={'class': 'custom-select'})  # Ajusta según el estilo que desees
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener las opciones dinámicamente según los modelos de categoría de las tres aplicaciones
        categoria_choices = []

        categoria_choices += [(f'audio_{categoria.id}', f'Audio y Video: {categoria.name}') for categoria in CategoriaAudioVideo.objects.all()]

        categoria_choices += [(f'equipo_{categoria.id}', f'Equipos: {categoria.name}') for categoria in CategoriaEquipos.objects.all()]
    
        categoria_choices += [(f'componente_{categoria.id}', f'Componentes: {categoria.name}') for categoria in categoriaComponentes.objects.all()]

        self.fields['category'].choices = categoria_choices