from django.shortcuts import render
from .models import Meccanico,Autovettura, Intervento

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def lista_meccanici(request):
    meccanici = Meccanico.objects.all()  # restituisce una lista di oggetti
    context = {'meccanici': meccanici}   # siccome render vuole un dizionario, inserisco la lista creata prima dentro un dizionario context
    return render(request,"lista_meccanici.html",context)