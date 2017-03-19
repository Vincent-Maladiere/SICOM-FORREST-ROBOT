""" Test de convergence de l'algorithme genetique """
from mvt_gene.genetics import *
#Definitions
nb_ind = 10 # nombres d'individus
mvt_nb = 3 # nombre de mouvements
proba_mut = 0.1 # probabilite de mutation
size_gene = 10 # taille d'une generation
size_ind = 10 # taille d'un individu
nb_ind_selec = 3 # nombre d'individu selectionné chaque generation
nb_run = 50 # nombre de simulation


def evaluation(liste) :
    return sum(liste)

def eval_gene(G) :
    for ind in G.liste : ind.give_score(evaluation)
    return

#Debut du script
gen = generation(size_gene,size_ind)
gen.ran_gen(mvt_nb)
eval_gene(gen)
print('#############')
print("Generation initiale")
gen.affiche()
print()
print('#############')
print("Lancement de l'algorithme genetique : ")
print()
print('Nombre de run :',nb_run, ' Proba de mutation :',proba_mut)
for i in range(0,nb_run):
    gen.next_gene(nb_ind_selec,proba_mut,mvt_nb,accouplement)
    eval_gene(gen)
gen.affiche()
