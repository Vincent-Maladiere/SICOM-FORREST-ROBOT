#!/usr/bin/env python3
""" Test de convergence de l'algorithme genetique """
import math
from mvt_gene.genetics import *

#############Definitions#############
nb_ind = 10 # nombres d'individus
mvt_nb = 3 # nombre de mouvements
proba_mut = 0.1 # probabilite de mutation
size_gene = 10 # taille d'une generation
size_ind = 10 # taille d'un individu
nb_ind_selec = 3 # nombre d'individu selectionné chaque generation
nb_run = 50 # nombre de simulation
nb_run_mean = 50 # nombre de lancement afin d'estimer la convergence en moyenne
nb_opt = [] # Vecteur de numeros de la generation ayant atteint la solution optimale

def evaluation(liste) :
    return sum(liste)

def eval_gene(G) :
    for ind in G.liste : ind.give_score(evaluation)
    return

def run_algogene():
    nb_opt = 0
    for i in range(0,nb_run):
        gen.next_gene(nb_ind_selec,proba_mut,mvt_nb,accouplement)
        if nb_opt == 0 :
            if gen.liste[0].liste == vec_opt.liste : nb_opt = gen.age-1
        eval_gene(gen)
    return nb_opt

#############Debut du script#############
gen = generation(size_gene,size_ind)
gen.ran_gen(mvt_nb)
eval_gene(gen)
vec_opt = individu(size_ind)
vec_opt.liste = [ mvt_nb-1 for i in range(size_ind)]
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
##for i in range(0,nb_run):
##    gen.next_gene(nb_ind_selec,proba_mut,mvt_nb,accouplement)
##    if nb_opt < 0 :
##        if gen.liste[0].liste == vec_opt.liste : nb_opt = gen.age-1
##    eval_gene(gen)


gen.affiche()

print()
if nb_opt[0] == 0 : print('Solution optimale non atteinte')
else :print('Solution optimale atteinte à la generation : ',nb_opt[0])

print()
print('#############')
print('Convergence en moyenne :')
print()

for i in range(nb_run_mean) :
    gen.ran_gen(mvt_nb)
    eval_gene(gen)
    nb_opt+=[run_algogene()]
nb_conv = 0

for i in range(nb_opt.count(0)) : nb_opt.remove(0)
nb_conv = len(nb_opt)
mean_conv = sum(nb_opt)/nb_conv
print('Avec nb_run_mean :',nb_run_mean,'| Proba_mut :',proba_mut,' | nb_run :',nb_run,' | nb_ind_selec :',nb_ind_selec)
print('La convergence est atteinte en moyenne a la ', int(mean_conv),' generation')
print(nb_conv,' generations ont convergées')
print('Maximum : ',max(nb_opt),' Minimum : ', min(nb_opt) )
nb_conv_var = sum( [ (i-mean_conv)**2 for i in nb_opt ] )/nb_conv
print('Variance :', math.sqrt(nb_conv_var))
