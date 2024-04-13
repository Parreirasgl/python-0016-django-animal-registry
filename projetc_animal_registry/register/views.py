from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

def editar_registro(request, cliente_id):
    cliente = Animal.objects.get(id=cliente_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('confirmacao')
    else:
        form = AnimalForm(instance=cliente)
    return render(request, 'editar_registro.html', {'form': form})

def confirmacao(request):
    return render(request, '/successo.html', {
        })
