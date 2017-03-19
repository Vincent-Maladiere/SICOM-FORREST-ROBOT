"""Test de l'algorithme genetique"""
from mvt_gene.genetics import *
nb_ind = 10 #
mvt_nb = 50 #
proba_mut = 0.01 #
size_gene = 10
size_ind = 10
nb_ind_selec = 3
print()
print('###############')
print('Initialisation')
print()
gene1=generation(size_gene,size_ind)
gene1.ran_gen(mvt_nb)
gene1.affiche()
print()
print('Utilisation fonction d evaluation')
print()
for i in gene1.liste:
    i.give_score(evaluation)
gene1.affiche()

print()
print('###############')
print('Test TRI')
print()
gene1.tri()
gene1.affiche()

print()

print('###############')
print('Test Copy')
print()

gene2=gene1.copy()

print('gene2 == gene1 : ', gene2==gene1)
print()
print('Affichage gene2 :')
gene2.affiche()
print()
print('###############')
print('Test Next Generation, Accouplement + mutation')
print()
print('Generation suivante, en ne gardant que ', nb_ind_selec , ' individus :')
print('Avec une proba de mutation fixee a ', proba_mut )

gene1.next_gene(nb_ind_selec,proba_mut,mvt_nb,accouplement)

gene1.affiche()
