from django.shortcuts import render
from .models import Compromisso
 
def hello_view(request):
    return render(request, 'index.html', {})

def list_compromissos(request):
    items = Compromisso.obsjects.all()
    return render(request, 'lista.html', {'items': items})