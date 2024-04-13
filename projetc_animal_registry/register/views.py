from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

def buscar(request):
    query = request.GET.get('input', '')  
    if query:  
        try:
            objeto_filtrado = Animal.objects.filter(nome=query) | Animal.objects.filter(codigo=query)
            if objeto_filtrado:
                nome_animal = objeto_filtrado.first().nome
            return redirect('path_editar_registro', nome_animal)
        except:
            return render(request, 'register/busca.html', {'input': False})   
    return render(request, 'register/busca.html', {'input': True})

def editar_registro(request, nome_animal):
    animal = Animal.objects.get(nome=nome_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('path_confirmar')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'register/editar_registro.html', {'form': form})

def confirmar(request):
    return render(request, 'register/confirmacao.html')


