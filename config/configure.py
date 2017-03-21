import parameters as Pa

def create_Mvt_MAT() :
    """ Genere la matrice de mouvements """
    for i in Pa.PIN_HL :
        for j in Pa.DEG_HL :
            Pa.MVT_MAT += [(i,j)]
    for i in Pa.PIN_ROT :
        for j in Pa.DEG_ROT :
            Pa.MVT_MAT += [(i,j)]
    return

def import_MVT_SET() :

    from MVT_SET import MVT_SET
    for i in MVT_SET :
        for j in i :
            j=Pa.MVT_MAT.index(j)
    return

def user_conf() :

    if Pa.MODE_PARAMETRAGE == 1 :
        import_MVT_SET()
    else

def config_file(filename) :
    f = open(filename,'wb')
    
    
