"""PARAMETRES NON MODIFIABLES"""
"""Modes de fonctionnement"""
MODE_SBS,MODE_DEBUG,MODE_NORMAL = 0,1,2
"""Matrice des mouvements"""
MVT_MAT = []
"""Matrice de reference"""
MVT_REF = []

"""PARAMETRES MODIFIABLES"""
"""Parametres de l'algo genetique """
MVT_NB = 3
NB_RUN = 50
SIZE_G = 10
SIZE_I = 10
PROBA_MUT = 0.1
NB_IND_SLT = 3
NB_RUN_MEAN = 50

""" Parametres moteurs """
PIN_HL = [11, 9, 3, 7, 8]
DEG_HL = [ 0, 90 ]
PIN_ROT = [ 14, 2, 5, 6, 10]
DEG_ROT = [ 0, 45, 90 ]

""" Parametrage de mouvements predefinis """
MODE_PARAMETRAGE = 1
