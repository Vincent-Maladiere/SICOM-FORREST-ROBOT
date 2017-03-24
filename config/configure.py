
import parameters as PA

def create_Mvt_MAT() :
    """ Genere la matrice de mouvements """
    for i in PA.PIN_HL :
        for j in PA.DEG_HL :
            PA.MVT_MAT += [(i,j)]
    for i in PA.PIN_ROT :
        for j in PA.DEG_ROT :
            PA.MVT_MAT += [(i,j)]
    return

def trslt_MVT_SET() :

    for i in PA.MVT_SET :
        for j in i :
            j=PA.MVT_MAT.index(j)

def user_conf() :

    if PA.MODE_PARAMETRAGE == 1 :
        import_MVT_SET()

def config_file(filename) :
    f = open(filename,'wb')
    s= 2 + 2 + len(PA.MVT_MAT)*2
    f.write(b'\xAA')
    size = s.bit_length()//8 +1
    if size > 2 :
        raise Exception('Fichier de configuration trop grand ')
    f.write(s.to_bytes(2,'big'))
    for i in PA.MVT_MAT :
        f.write(bytes(i))
    f.write(b'\xFF')
    f.close()

    
    
    
    
