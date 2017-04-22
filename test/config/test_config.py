import sys
sys.path[0] = sys.path[0].replace('/test/config','')

import parameters as PA
import mvt_gene.class_genetics as CG
import mvt_gene.fct_genetics as FG
import config.configure as cfg
import binascii

print()
print('###############')
print('Initialisation')
print()
PA.MODE_PARAMETRAGE = 0
cfg.user_conf()
gene1=CG.generation(PA.SIZE_G,PA.SIZE_I)
gene1.ran_gen()
for i in gene1.liste:
    i.give_score(PA.FCT_EVAL)
    
gene1.affiche()
print()

print('Affichage de la matrice de mouvement')
print(PA.MVT_MAT)
print('Affichage de la matrice de reference utilisée')
print(PA.MVT_REF)
f = open('RobotCfg.bin','rb')
print(binascii.b2a_hex(f.read()))
f.close()

print('Creation des 3 premiers fichiers binaires individu et affichage')
for i in range(3) :
    print()
    print('Individu ',i)
    s = 'Individu_' + str(i) + '.bin'
    cfg.ind_file(gene1.liste[i],filename=s)
    gene1.liste[i].affiche()
    f=open(s,'rb')
    print(binascii.b2a_hex(f.read()))
    f.close()
