
import parameters as PA
import mvt_gene.class_genetics as CG

def create_MVT_MAT() :
    """ Genere la matrice de mouvements """
    for i in PA.PIN_HL :
        for j in PA.DEG_HL :
            PA.MVT_MAT += [(i,j)]
    for i in PA.PIN_ROT :
        for j in PA.DEG_ROT :
            PA.MVT_MAT += [(i,j)]
    return

def trslt_MVT_SET() :
    """Traduit la matrice donnée en elements de la matrice de mouvements"""
    PA.MVT_REF=[]
    l=[]
    for i in PA.MVT_SET :
        if type(i) == list :
            for j in i :
                try :
                    l+=[PA.MVT_MAT.index(j)]
                except ValueError :
                    raise ValueError('Veuillez redéfinir la matrice MVT_SET dans le module paramêtres, le tuple ',j,' n a pas ete trouve dans la matrice de mouvement MVT_MAT ')
            PA.MVT_REF+=[l]
        else :
            try :
                PA.MVT_REF+=[PA.MVT_MAT.index(i)]
            except ValueError :
                raise ValueError('Veuillez redéfinir la matrice MVT_SET dans le module paramêtres, le tuple ',j,' n a pas ete trouve dans la matrice de mouvement MVT_MAT ')
            

def user_conf(,,filename='RobotCfg.bin') :
    create_MVT_MAT()
    config_file(filename)
    if PA.MODE_PARAMETRAGE == 1 :
        trslt_MVT_SET()
    elif PA.MODE_PARAMETRAGE == 0 :
        PA.MVT_REF = [ i for i in range(len(PA.MVT_MAT)) ]
    PA.MVT_NB = len(PA.MVT_REF)


def config_file(filename) :
    f = open(filename,'wb')
    s= 2 + 2 + len(PA.MVT_MAT)*2
    f.write(b'\xAA')
    if size > 65536 :
        raise Exception('Fichier de configuration trop grand ')
    f.write(s.to_bytes(2,'big'))
    for i in PA.MVT_MAT :
        f.write(bytes(i))
    f.write(b'\xFF')
    f.close()

def ind_file(filename,individu) :
    f = open(filename,'wb')
    f.write(b'\xAA')
    s=1
    f.write(b'\x0000')
    s+=2
    for i in individu.liste :
        if type(PA.MVT_REF[i]) == list :
            for j in PA.MVT_REF[i] :
                f.write(bytes(j))
                s+=1
            f.write(b'\0xFA')
            s+=1
        else :
            f.write(PA.MVT_REF[i])
            f.write(b'\0xFA')
            s+=1
    f.write(b'\0xFF')
    s+=1
    if size > 65536 :
        raise Exception('Fichier de configuration trop grand ')
    f.seek(1,0)
    f.write(s.to_bytes(2,'big'))
    f.close()
