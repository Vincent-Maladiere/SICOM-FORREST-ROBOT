# -*- coding: utf-8 -*-
import mvt_gene.fct_genetics as FG


# PARAMETRES NON MODIFIABLES
# Modes de fonctionnement global
MODE_SBS,MODE_DEBUG,MODE_NORMAL = 0,1,2
NO_DISPLAY,DISPLAY = 0,1

# Matrices de l'algo genetique
## Matrice des mouvements
MVT_MAT = []
## Matrice de reference
MVT_REF = []

# Parametres image_proc
DISPLAY = 1
NO_DISPLAY = 0

# Parametres config
BSIZE_IND = 1 # Taille maximal en octet pour les fichiers binaires des individus
SIZE_IND = 2**(8*BSIZE_IND) - 1
BSIZE_CONF = 2 # Idem pour le fichier binaire de configuration
SIZE_CONF = 2**(8*BSIZE_CONF) - 1

# PARAMETRES MODIFIABLES
# Parametres de l'algo genetique
MVT_NB = 3
NB_RUN = 50
SIZE_G = 10
SIZE_I = 10
NB_IND_SLT = 3
NB_RUN_MEAN = 50


# Parametres de l'algo de traitement d'image

MODE_IMPROC = NO_DISPLAY

THRES_G_HUE_LOWER = 40      #green
THRES_G_HUE_UPPER = 60
THRES_G_SAT_LOWER = 20

THRES_R_HUE_LOWER = 0       #red
THRES_R_HUE_UPPER = 15
THRES_R_SAT_LOWER = 100

THRES_VALUE_LOWER = 200

A4_REAL_DIAGO = 35.96 #cm


##Fonctions choisies dans le module fct_genetics du paquet mvt_gene
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

# Matrice de mouvements imposés
MVT_SET = []

# Paramétre de fonctionnement
MODE_PARAMETRAGE = 1
