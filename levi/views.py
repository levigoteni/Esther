from django.shortcuts import render
from .models import Geek

# Create your views here.
def Accueil(request):
	return render(request, "levi/accueil.html")

def Etudiant(request):
	context= {"etudiant":Geek.objects.all()}
	return render(request, "levi/list_etudiant.html", context)

def Levi(request, id):
	context= {
		"etudiant":Geek.objects.get(id = id),
	}
	return render(request, "levi/etudiants.html", context)

