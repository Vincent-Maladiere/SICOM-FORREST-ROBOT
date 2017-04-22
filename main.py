#!/bin/python3
# -*- coding: utf-8 -*-
import config
import sys
import mvt_gene
import parameters

def main() :

    for i in sys.argv[1:]:
        exec(i)
    config.configure.user_conf()
    mvt_gene.main_genetics.main()
    return
main()