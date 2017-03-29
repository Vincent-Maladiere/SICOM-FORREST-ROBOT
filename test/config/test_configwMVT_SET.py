import sys,random
sys.path[0] = sys.path[0].replace('/test/config','')

import parameters as PA
import mvt_gene.class_genetics as CG
import mvt_gene.fct_genetics as FG
import config.configure as cfg
import binascii

for i in sys.argv[1:] :
    exec(i)
print()
print('###############')
print('Initialisation')
print()
PA.MODE_PARAMETRAGE = 1
PA.MVT_SET = []
SIZE_MVT_SET = 6
SIZE_LINE = 4

cfg.create_MVT_MAT()
for i in range(SIZE_MVT_SET):
    PA.MVT_SET+=[ [ PA.MVT_MAT[random.randrange(len(PA.MVT_MAT))] for i in range(random.randrange(1,SIZE_LINE)) ] ]
cfg.config_file('RobotCfg.bin')
if PA.MODE_PARAMETRAGE == 1 :
    cfg.trslt_MVT_SET()
elif PA.MODE_PARAMETRAGE == 0 :
    PA.MVT_REF = [ i for i in range(len(PA.MVT_MAT)) ]
PA.MVT_NB = len(PA.MVT_REF)


gene1=CG.generation(PA.SIZE_G,PA.SIZE_I)
gene1.ran_gen()
for i in gene1.liste:
    i.give_score(PA.FCT_EVAL)
    
gene1.affiche()

print()
print('Affichage de la matrice de mouvement')
print(PA.MVT_MAT)
print('Affichage de la matrice de mouvements donnée')
print(PA.MVT_SET)
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
    cfg.ind_file(s,gene1.liste[i])
    gene1.liste[i].affiche()
    f=open(s,'rb')
    print(binascii.b2a_hex(f.read()))
    f.close()
