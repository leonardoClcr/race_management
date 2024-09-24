from django.shortcuts import redirect, render
from corredores.models import Corredores
from corredores.forms import CorredorModelForm


def corredores_view(request):
    corredores = Corredores.objects.all()
    return render(request, 'corredores.html', context={'corredores': corredores})


def new_corredor(request):
    if request.method == 'POST':
        new_corredor_form = CorredorModelForm(request.POST)
        if new_corredor_form.is_valid():
            new_corredor_form.save()
            return redirect('corredores')
    else:
        new_corredor_form = CorredorModelForm()
    return render(request, 'new_corredor.html', {'new_corredor_form': new_corredor_form})