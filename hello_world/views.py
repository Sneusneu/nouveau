from django.http import HttpResponse
from django.shortcuts import render
import operator

def base(request):
    return render(request,'base.html')

def compteur(request):
    return render(request,'compteur.html')

def affiche(request):
    compteur_mots = request.GET['texte']
    liste_mots = compteur_mots.split()

    print(compteur_mots)

    word_dict = {}
    #affichez les mots avec leurs nombre d'apparitions dans le texte
    for mot in liste_mots :
        if mot in word_dict:
            #augmenter la valeur de 1 de la clé mot
            word_dict[mot] +=1
        else:
            #donner la valeur 1 à la clé mot
            word_dict[mot] = 1

    to_sort = sorted(word_dict.items(), key = operator.itemgetter(1), reverse = True)
    print(to_sort)
    return render(request,'affiche.html', {'compteur_mots': compteur_mots, 'liste_mots': len(liste_mots),'to_sort':to_sort})

