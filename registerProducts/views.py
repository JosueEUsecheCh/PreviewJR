from django.shortcuts import render, redirect
from .forms import register_products
from JRAudio_video.models import CategoriaAudioVideo, ComponenteAudioVideo
from JREquipos.models import CategoriaEquipos, Equipo
from JRComponentes.models import categoriaComponentes, Componentes

def product_register(request):
    if request.method == 'POST':
        form = register_products(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            price = form.cleaned_data['price']
            avaiability = form.cleaned_data['avaiability']
            category_data = form.cleaned_data['category']
            
            try:
                prefix, category_id = category_data.split('_')
                category_id = int(category_id)
                
                if prefix == 'audio':
                    categoria = CategoriaAudioVideo.objects.get(id=category_id)
                    componente = ComponenteAudioVideo(name=name, description=description, images=image, price=price, category=categoria, avaiability=avaiability)
                    componente.save()
                
                elif prefix == 'equipo':
                    categoria = CategoriaEquipos.objects.get(id=category_id)
                    componente_equipo = Equipo(name=name, description=description, images=image, price=price, category=categoria, avaiability=avaiability)
                    componente_equipo.save()
                    
                elif prefix == 'componente':
                    categoria = categoriaComponentes.objects.get(id=category_id)
                    componente_componente = Componentes(name=name, description=description, images=image, price=price, category=categoria, avaiability=avaiability)
                    componente_componente.save()
                
                else:
                    return render(request, 'error.html', {'message': 'Categoría no encontrada'})
                
                return redirect('products')  # Ajusta el nombre de la URL de éxito según tu configuración
            
            except ValueError:
                return render(request, 'error.html', {'message': 'Error en la selección de categoría'})
    
    else:
        form = register_products()
    
    return render(request, 'product_register/product_register.html', {'form': form})
