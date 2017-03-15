import genetics,random

taille_genome=4
nb_mvt=5
taille_pop=6
selec=3
proba_mutation=0.01
gen1=genetics.generation(taille_pop, taille_genome)
gen1.ran_gen(nb_mvt)
for i in range(taille_pop) :
    gen1.liste[i].score=random.randrange(10)
print '######nouvelle generation######\n'
gen1.affiche()
gen2=gen1.next_gene(selec, proba_mutation, nb_mvt)
for i in range(taille_pop-selec, taille_pop) :
    gen2.liste[i].score=random.randrange(10)
print '######nouvelle generation######\n'
gen2.affiche()
gen3=gen2.next_gene(selec, proba_mutation, nb_mvt)
print '######nouvelle generation######\n'
gen3.affiche()
