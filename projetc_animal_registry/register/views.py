from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

def editar_registro(request):
    animal = Animal.objects.get(codigo=1)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('confirmacao')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'editar_registro.html', {'form': form})

def confirmacao(request):
    return render(request, '/successo.html', {
        })
