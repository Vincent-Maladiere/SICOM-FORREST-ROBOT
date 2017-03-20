"""PARAMETRES NON MODIFIABLES"""
"""Modes de fonctionnement"""
MODE_SBS,MODE_DEBUG,MODE_NORMAL = 0,1,2
"""Matrice des mouvements"""
MVT_MAT = []
"""Matrice de reference"""
MVT_REF = []



"""PARAMETRES MODIFIABLES"""

"""Parametres individus et populations"""
NB_POP = 100
vec_length = 10
vec_columns = 1

""" Parametres moteurs """
PIN_HL = [11, 9, 3, 7, 8]
DEG_HL = [ 0, 90 ]
PIN_ROT = [ 14, 2, 5, 6, 10]
DEG_ROT = [ 0, 45, 90 ]

""" Parametrage de mouvements predefinis """
MODE_PARAMETRAGE = 1
