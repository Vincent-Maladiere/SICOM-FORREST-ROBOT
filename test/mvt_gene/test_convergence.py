#!/usr/bin/env python3
""" Test de convergence de l'algorithme genetique """
import math,sys
sys.path[0] = sys.path[0].replace('/test/mvt_gene','')
from mvt_gene.genetics import *

#############Definitions#############
####Variables####
##A priori les variables ci-dessous seront determinés par la pratique##
mvt_nb = 3 # nombre de mouvements
nb_run = 50 # nombre de simulation
size_i = 10 # taille d'un individu

##Les 3 variables ci-dessous seront celles à optimiser pour atteindre le plus rapidement la convergence##

proba_mut = 0.1 # probabilite de mutation
size_g = 10 # taille d'une generation
nb_ind_slt = 3 # nombre d'individu selectionné chaque generation


nb_run_mean = 50 # nombre de lancement afin d'estimer la convergence en moyenne, elle devrait au moins être supérieur à la moyenne + variance 

##Ci dessous la fonction d'evaluation définissant l'individu optimal##
def evaluation(liste) :
    return sum(liste)

def eval_gene(G) :
    for ind in G.liste : ind.give_score(evaluation)
    return

def run_algogene():
    nb_opt = 0
    for i in range(0,nb_run):
        gen.next_gene(nb_ind_slt,proba_mut,mvt_nb,accouplement)
        if nb_opt == 0 :
            if gen.liste[0].liste == vec_opt.liste : nb_opt = gen.age-1
        eval_gene(gen)
    return nb_opt

#############Debut du script#############
nb_opt = [] # Vecteur de numeros de la generation ayant atteint la solution optimale
filename = None # Nom de fichier de sorti

for i in sys.argv[1:] :
    exec(i)
    
gen = generation(size_g,size_i)
gen.ran_gen(mvt_nb)
eval_gene(gen)
vec_opt = individu(size_i)
vec_opt.liste = [ mvt_nb-1 for i in range(size_i)]
vec_opt.give_score(evaluation)

print('#############')
print("Generation initiale")
gen.affiche()
print()
print('Solution optimale atteinte pour le vecteur : ')
vec_opt.affiche()
print()
print('#############')
print("Lancement de l'algorithme genetique : ")
print()
print('Nombre de run :',nb_run, ' Proba de mutation :',proba_mut)

nb_opt+=[run_algogene()]

gen.affiche()

print()
if nb_opt[0] == 0 : print('Solution optimale non atteinte')
else :print('Solution optimale atteinte à la generation : ',nb_opt[0])

print()
print('#############')
print('Convergence en moyenne :')
print()
nb_opt = []
for i in range(nb_run_mean) :
    gen.ran_gen(mvt_nb)
    eval_gene(gen)
    nb_opt+=[run_algogene()]
nb_conv = 0
for i in range(nb_opt.count(0)) : nb_opt.remove(0)
nb_conv = len(nb_opt)
print('Avec nb_run_mean :',nb_run_mean,'| proba_mut=',proba_mut,' | nb_run=',nb_run,' | nb_ind_slt=',nb_ind_slt)
print('size_g=',size_g,'| size_i=',size_i,'| mvt_nb=',mvt_nb) 
if nb_conv > 0 :
    mean_conv = sum(nb_opt)/nb_conv
    print('La convergence est atteinte en moyenne a la ', int(mean_conv),' generation')
    print(nb_conv,' generations ont convergées')
    print('Maximum : ',max(nb_opt),' Minimum : ', min(nb_opt) )
else : print('Aucune generation n a atteint la solution optimale')

if nb_conv > 1 :
    nb_conv_var = sum( [ (i-mean_conv)**2 for i in nb_opt ] )/(nb_conv-1)
    print('Variance :', math.sqrt(nb_conv_var))
else :print('Variance : ##Impossible à évaluer : division par 0##')
