#!/usr/bin/env python3
""" Test de convergence de l'algorithme genetique """
import math,sys
sys.path[0] = sys.path[0].replace('/test/mvt_gene','')
import mvt_gene.class_genetics as CG
import parameters as PA
import mvt_gene.fct_genetics as FG

#############Definitions#############
####Variables####
##A priori les variables ci-dessous seront determinés par la pratique##
PA.MVT_NB = 3 # nombre de mouvements
PA.NB_RUN = 50 # nombre de simulation
PA.SIZE_I = 10 # taille d'un individu

fct_accoupl = FG.accouplement
fct_evaluation = FG.evaluation
fct_mutation = FG.mutation

##Les 3 variables ci-dessous seront celles à optimiser pour atteindre le plus rapidement la convergence##

PA.PROBA_MUT = 0.1 # probabilite de mutation
PA.SIZE_G = 10 # taille d'une generation
PA.NB_IND_SLT = 3 # nombre d'individu selectionné chaque generation

nb_run_mean = 50 # nombre de lancement afin d'estimer la convergence en moyenne, elle devrait au moins être supérieur à la moyenne + variance 

##Ci dessous la fonction d'evaluation définissant l'individu optimal##
def evaluation(liste) :
    return sum(liste)

def eval_gene(G) :
    for ind in G.liste : ind.give_score(evaluation)
    return

def run_algogene():
    nb_opt = 0
    for i in range(0,PA.NB_RUN):
        gen.next_gene(fct_accoupl,fct_mutation)
        if nb_opt == 0 :
            if gen.liste[0].liste == vec_opt.liste : nb_opt = gen.age-1
        eval_gene(gen)
    return nb_opt

#############Debut du script#############
nb_opt = [] # Vecteur de numeros de la generation ayant atteint la solution optimale
filename = None # Nom de fichier de sorti

for i in sys.argv[1:] :
    exec(i)
    
gen = CG.generation(PA.SIZE_G,PA.SIZE_I)
gen.ran_gen()
eval_gene(gen)
vec_opt = CG.individu(PA.SIZE_I)
vec_opt.liste = [ PA.MVT_NB-1 for i in range(PA.SIZE_I)]
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
print('Nombre de run :',PA.NB_RUN, ' Proba de mutation :',PA.PROBA_MUT)

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
    gen.ran_gen()
    eval_gene(gen)
    nb_opt+=[run_algogene()]
nb_conv = 0
for i in range(nb_opt.count(0)) : nb_opt.remove(0)
nb_conv = len(nb_opt)
print('Avec nb_run_mean :',nb_run_mean,'| proba_mut=',PA.PROBA_MUT,' | nb_run=',PA.NB_RUN,' | nb_ind_slt=',PA.NB_IND_SLT)
print('size_g=',PA.SIZE_G,'| size_i=',PA.SIZE_I,'| mvt_nb=',PA.MVT_NB) 
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
