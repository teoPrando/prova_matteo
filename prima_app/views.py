from django.shortcuts import render,redirect
from .models import Meccanico,Autovettura, Intervento
from .forms import MeccanicoForm,AutovetturaForm

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def meccanici(request):
    meccanici = Meccanico.objects.all()  # restituisce una lista di oggetti
    errori=False #serve per capire se c'è stato un errore nella validazione dei dati
    """
    request.method può ritornare due valori:
    -GET: Quando viene aperta la pagina (url o link)
    -POST: quando viene compilato il form e cliccato su salva
    """
    if request.method == "POST":  # quando viene cliccato su salva la richiesta HTTP è di tipo POST
        form = MeccanicoForm(request.POST) # viene creato il form con i valori inseriti nei campi
        """
        ESEMIO: nei campi inserisco nome="Mario", cognome="Rossi", clicco su salva:
        -request.POST contiene: {'nome': 'Mario', 'cognome': 'Rossi'}
        """
        if form.is_valid(): # controlla che i campi non siano vuoti e fa tutte le validazioni, in questo caso solo max_length=20, se è tutto aposto ritorna TRUE
            form.save() # crea l'oggetto meccanico e lo salva nel database
            return redirect('prima_app:lista_meccanici') #ricarica la pagina con una richiesta di tipo GET (vengono tolti i valori inseriti dal form e visualizzato nella lista il meccanico inserito)
        else: #se i dati inseriti non sono coretti (es:targa non valida o campo vuoto)
            errori=True
    else: # quando viene semplicemente caricata la pagina la richiesta è di tipo GET
        form = MeccanicoForm() # viene resettato il form con i campi dove inserire i valori vuoti
    context = {'meccanici': meccanici,'form':form,'errori':errori}   # siccome render vuole un dizionario, inserisco la lista_meccanici e il form creati prima dentro un dizionario context
    return render(request,"lista_meccanici.html",context)

def autovetture(request):
    macchine = Autovettura.objects.all()  # restituisce una lista di oggetti
    errori=False #serve per capire se c'è stato un errore nella validazione dei dati
    if request.method == "POST":  # quando viene cliccato su salva la richiesta HTTP è di tipo POST
        form = AutovetturaForm(request.POST) # viene creato il form con i valori inseriti nei campi
        if form.is_valid(): # controlla che i campi non siano vuoti e fa tutte le validazioni, se è tutto aposto ritorna TRUE
            form.save() # crea l'oggetto autovettura e lo salva nel database
            return redirect('prima_app:lista_autovetture') #ricarica la pagina con una richiesta di tipo GET (vengono tolti i valori inseriti dal form)
        else: #se i dati inseriti non sono coretti (es:targa non valida o campo vuoto)
            errori=True
    else: # quando viene semplicemente caricata la pagina la richiesta è di tipo GET
        form = AutovetturaForm() # viene resettato il form con i campi dove inserire i valori vuoti
    context = {'macchine': macchine,'form':form,'errori':errori}   # siccome render vuole un dizionario, inserisco la lista delle macchine e il form creati prima dentro un dizionario context
    return render(request,"lista_autovetture.html",context)