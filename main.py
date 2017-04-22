#!/bin/python3
# -*- coding: utf-8 -*-
import config
import mvt_gene

def main() :
    config.configure.user_conf()
    mvt_gene.main_genetics.main()
    return
main()