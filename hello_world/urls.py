from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('compteur/', views.compteur),
    path('affiche/', views.affiche, name="affiche")
]
