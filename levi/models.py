from django.db import models

class Geek(models.Model):
    nom= models.CharField(max_length= 25)
    prenom= models.CharField(max_length=25)
    matricule= models.CharField(max_length=25)
    age= models.IntegerField()
    niveau= models.CharField(max_length=25)
    filiere= models.CharField(max_length=25)
    AnneeA= models.CharField(max_length=25)
    photo= models.ImageField(upload_to="levi/media")

    def __str__(self):
	    return self.nom
