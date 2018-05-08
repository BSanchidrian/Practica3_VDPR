from django.http import HttpResponse
from django.shortcuts import render

from .forms import InputForm

def index(request):
    form = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # TODO
            input_received = form.cleaned_data['input']
            print(input_received)
    else:
        form = InputForm()

    context = {
        'palabras': ['Hola', 'Adios'],
        'form': form
    }
    return render(request, 'verificacion/index.html', context)