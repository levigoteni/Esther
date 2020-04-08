from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.Accueil),
    url(r'^list_etudiant', views.Etudiant),
    url(r'^etudiant/(?P<id>[0-9]+)$', views.Levi),

]
