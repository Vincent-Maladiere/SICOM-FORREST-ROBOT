#!/usr/bin/python3
# -*- coding: utf-8 -*-
import parameters as PA
import mvt_gene.class_genetics as CG
import config as cfg
#import communication as co

def main() :

    gen = CG.generation(PA.SIZE_G, PA.SIZE_I)
    gen.ran_gen()
    for i in range(PA.NB_RUN):
        run_gene(gen)


def run_gene(gen) :

    scalar=0
    for ind in gen.liste :

        # on cree le fichier correspondant à l'individu, il sera envoye par le module de communication ( par main_ind )
        cfg.configure.ind_file(ind) #


        # Ici on est cense recuperer la distance parcouru par le robot, elle est renvoyee par le main_ind du module communication
        # scalar = co.main_ind('ind.bin')

        PA.FCT_EVAL(ind,scalar) # On evalue l'individu avec la fonction d'evaluation indiquee par le module parameters.py

    gen.next_gene(PA.FCT_ACC,PA.FCT_MUT) # on genere la prochaine generation une fois que tous les individus ont ete evalues


