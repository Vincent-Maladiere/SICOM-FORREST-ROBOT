import parameters as PA
import sys

def create_MVT_MAT() :
    """ Genere la matrice de mouvements """
    for i in PA.PIN_HL :
        for j in PA.DEG_HL :
            PA.MVT_MAT += [(i,j)]
    for i in PA.PIN_ROT :
        for j in PA.DEG_ROT :
            PA.MVT_MAT += [(i,j)]

def trslt_MVT_SET() :
    """Traduit la matrice donnee en une matrice composee d'indice de la matrice de mouvements"""
    PA.MVT_REF=[]
    for i in PA.MVT_SET :
        l=[]
        if type(i) == list : # Si c'est une liste c'est une sequence de mouvements effectués en meme temps
            for j in i :
                try : # (1) Ici on regarde si les tuples donnés dans la matrice MVT_SET sont disponibles dans la matrice de mouvements
                    l+=[PA.MVT_MAT.index(j)]
                except ValueError :
                    raise ValueError('Veuillez redéfinir la matrice MVT_SET dans le module paramêtres, le tuple ',j,' n est pas défini dans la matrice de mouvement MVT_MAT ')
            PA.MVT_REF+=[l]

        else : # Pareil qu'en (1)
            try :
                PA.MVT_REF+=[PA.MVT_MAT.index(i)]
            except ValueError :
                raise ValueError('Veuillez redéfinir la matrice MVT_SET dans le module paramêtres, le tuple ',j,' n est pas défini dans la matrice de mouvement MVT_MAT ')


def user_conf(filename='RobotCfg.bin') :
    ##Execution des instructions passées en argument ( changement de mode, changement des fonctions utilisées )
    for i in sys.argv[1:]:
        exec(i)
    #Creation de la matrice de mouvement
    create_MVT_MAT()
    #Creation du fichier de configuration pour l'arduino
    config_file(filename)

    if PA.MODE_PARAMETRAGE == 1 :
        # En mode parametrage on cree une matrice de reference en rapport
        # avec la matrice de sequence de mouvement voulu
        trslt_MVT_SET()
    elif PA.MODE_PARAMETRAGE == 0 : # Sinon on la matrice de refe
        PA.MVT_REF = [ i for i in range(len(PA.MVT_MAT)) ]
    # On met a jour le nombre de mouvements possible
    PA.MVT_NB = len(PA.MVT_REF)


def config_file(filename) :
    """Genere le fichier de configuration binaire"""

    f = open(filename,'wb')
    s= 2 + PA.BSIZE_CONF + len(PA.MVT_MAT)*2
    #L'entete du fichier commence par 0xAA
    f.write(b'\xaa')
    #La taille du fichier est limite par BSIZE_CONF du module parameters.py
    if s > PA.SIZE_CONF :
        raise Exception('Fichier de configuration trop grand ')
    ##La taille du fichier est écrit sur 2 octets
    f.write(s.to_bytes(PA.BSIZE_CONF,'big'))
    #####
    #On pourrait écrire sur qqes octets les différents paramétres avec lesquels on veut que l'arduino s'execute
    #Par exemple les Modes d'execution ( Mode step by step, mode debug, mode normal )
    #La vitesse d'execution des mouvements
    #etc ....
    #
    #f.write(...)
    #
    #
    #####

    ###On ecrit ensuite ici la matrice de mouvement
    for i in PA.MVT_MAT :
        f.write(bytes(i))
    #On indique la fin du fichier avec 0xFF
    f.write(b'\xFF')

    f.close()

def ind_file(individu,filename='ind.bin') :
    """Fonction ecrivant dans un fichier binaire le code genetique d'un individu"""
    f = open(filename,'wb')
    #Ecriture de l'entete du fichier
    f.write(b'\xAA')
    s=1 # s compte les octets ecrit
    # On reserve ici qqes octet pour ecrire la taille, on connaitra la taille a la fin du fichier

    f.write(bytes(PA.BSIZE_IND))
    s+=PA.BSIZE_IND

    for i in individu.liste :
        #On parcourt elements de la liste
        #Si l'element est une liste alors les mouvements qui la composent doivent etre executé en parallele
        #Sinon l'element est un singleton et il sera execute sequentiellement
        #Les mouvements qui sont executes en meme temps sont entre deux 0xFA  ( a par pour le premier element de la liste)

        if type(PA.MVT_REF[i]) == list : # On a trouve une liste de mouvements execute en parallele ( sequence de mouvements )
            for j in PA.MVT_REF[i] :
                f.write(bytes([j]))
                s+=1
            f.write(b'\xFA') # on indique la fin de la sequence
            s+=1
        else : # mouvement seul
            f.write(bytes([PA.MVT_REF[i]]))
            f.write(b'\xFA') # on indique la fin de la sequence
            s+=2
    #Fin de l'individu indiqué par 0xFF
    f.write(b'\xFF')
    s+=1
    if s > PA.SIZE_IND : # la taille de l'individu est limité par SIZE_IND de parameters.PY
        raise Exception('Fichier de configuration trop grand ')
    #On se replace la ou on avait reserve une place pour ecrire la taille de l'individu
    f.seek(1,0)
    f.write(s.to_bytes(PA.BSIZE_IND,'big'))
    f.close()
