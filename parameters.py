# -*- coding: utf-8 -*-
import mvt_gene.fct_genetics as FG

# PARAMETRES NON MODIFIABLES
# Modes de fonctionnement
MODE_SBS,MODE_DEBUG,MODE_NORMAL = 0,1,2
# Matrice des mouvements
MVT_MAT = []
# Matrice de reference
MVT_REF = []

# PARAMETRES MODIFIABLES
# Parametres de l'algo genetique
MVT_NB = 3
NB_RUN = 50
SIZE_G = 10
SIZE_I = 10
NB_IND_SLT = 3
NB_RUN_MEAN = 50

# Fonctions choisies dans le module fct_genetics du paquet mvt_gene
FCT_MUT = FG.mutation2
FCT_EVAL = FG.evaluation
FCT_ACC = FG.accouplement
# Parametres des ces fonctions
PROBA_MUT = 0.1
MUT4_MAX = 5 # environ 3 mutations , pour calculer appliquer N*(1-(1-1/N)**(N+1)) à MUT4_MAX-1

# Parametres moteurs
PIN_HL = [11, 9, 3, 7, 8]
DEG_HL = [ 0, 90 ]
PIN_ROT = [ 14, 2, 5, 6, 10]
DEG_ROT = [ 0, 45, 90 ]

# Matrice de mouvements imposée
MVT_SET = []

# Paramétres de fonctionnement
MODE_PARAMETRAGE = 1
