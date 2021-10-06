from django.shortcuts import render
from.models import *
# Create your views here.

def index(request):
    allordenador = ordenador.objects.all()
    return render(request, 'index.html', {'allordenador':allordenador})
