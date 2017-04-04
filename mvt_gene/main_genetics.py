#!/usr/bin/python3
# -*- coding: utf-8 -*-
import parameters as PA
import mvt_gene.class_genetics as CG
import config as cfg
#import communication as co
#import imageproc as imp

def main() :

    gen = CG.generation(PA.SIZE_G, PA.SIZE_I)
    gen.ran_gen()
    for i in range(PA.NB_RUN):
        run_gene(gen)


def run_gene(gen) :
    scalar=0

    for ind in gen.liste :

        cfg.configure.ind_file(ind)
        # scalar = co.main_ind('ind.bin')
        PA.FCT_EVAL(ind,scalar)
    gen.next_gene(PA.FCT_ACC,PA.FCT_MUT)


