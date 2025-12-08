from django.db import models
from django.core.validators import RegexValidator,MinValueValidator

# Create your models here.

class Meccanico (models.Model):
    ID_meccanico=models.AutoField(primary_key=True) #auto-increment
    nome=models.CharField(max_length=20) #stringhe di lunghezza massima 20
    cognome=models.CharField(max_length=20)

    def __str__(self): #metodo toString
        return self.nome + " "+self.cognome

class Autovettura(models.Model):
    targa_validator = RegexValidator(
        regex=r'^[A-Z]{2}\d{3}[A-Z]{2}$', #Controlla il formato della targa (es: [A-Z]{2} significa che i primi 2 devono essere caratteri da A a Z, poi i prossimi 3 devono essere cifre (/d))
        message="La targa deve essere nel formato 'AB 123 CD', con lettere maiuscole e senza spazi" #messaggio che appare se non vengono soddisfatte le condizioni
    )
    targa = models.CharField(
        max_length=7,  # AB123CD = 7 caratteri
        primary_key=True,
        validators=[targa_validator] #controllo specificato prima
    )
    marca = models.CharField(max_length=20)
    modello = models.CharField(max_length=20)

    def __str__(self):
        return self.marca+" "+self.modello+" "+self.targa
    
class Intervento (models.Model):
    ID_intervento=models.AutoField(primary_key=True) #auto-increment
    meccanico=models.ForeignKey(Meccanico,on_delete=models.CASCADE,related_name="interventi")#foreign key che si collega alla tabella Maccanico
    #related_name: dopo aver letto un oggetto meccanico in una variabile 'meccanico' scrivendo meccanico.interventi.all() posso vedere tutti gli interventi di quel meccanico
    targa=models.ForeignKey(Autovettura,on_delete=models.CASCADE,related_name="interventi")#foreign key che si collega alla tabella Autovetture
    problema = models.TextField()
    costo = models.DecimalField(
        max_digits=10,          # numero totale di cifre
        decimal_places=2,       # numero di decimali
        validators=[MinValueValidator(0.01)]  # maggiore di 0 (SQL --> costo DECIMAL(10,2) CHECK(costo>0))
    )


    def __str__(self): #metodo toString
        return f"{self.problema} ({self.costo}€) - {self.meccanico} - {self.targa}"