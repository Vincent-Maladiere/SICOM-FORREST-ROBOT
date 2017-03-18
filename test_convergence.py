""" Test de convergence de l'algorithme genetique """
from mvt_gene.genetics import *
#Definitions
nb_ind = 10 #
mvt_nb = 2 #
proba_mut = 0.01 #
size_gene = 10
size_ind = 10
nb_ind_selec = 3
nb_run = 100


def evaluation(liste) :
    return sum(liste)

def eval_gene(G) :
    for ind in G.liste : ind.give_score(evaluation)
    return

#Debut du script
gen = generation(size_gene,size_ind)
gen.ran_gen(mvt_nb)
eval_gene(gen)
print("Generation initiale")
gen.affiche()
print()
print("Lancement de l'algorithme genetique : ")
print()
for i in range(0,nb_run):
    gen.next_gene(nb_ind_selec,proba_mut,mvt_nb,accouplement)
    eval_gene(gen)
gen.affiche()
