"""Test de l'algorithme genetique"""
import sys
sys.path[0] = sys.path[0].replace('/test/mvt_gene','')
import mvt_gene.class_genetics as CG
import mvt_gene.fct_genetics as FG
import parameters as PA


fct_accoupl = FG.accouplement
fct_evaluation = FG.evaluation
fct_mutation = FG.mutation2
for i in sys.argv[1:] :
    exec(i)
print()
print('###############')
print('Initialisation')
print()
gene1=CG.generation(PA.SIZE_G,PA.SIZE_I)
gene1.ran_gen()
gene1.affiche()
print()
print('Utilisation fonction d evaluation')
print()
for i in gene1.liste:
    i.give_score(fct_evaluation)
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
print('Generation suivante, en ne gardant que ', PA.NB_IND_SLT , ' individus :')
print('Avec une proba de mutation fixee a ', PA.PROBA_MUT )

gene1.next_gene(fct_accoupl,fct_mutation)

gene1.affiche()
