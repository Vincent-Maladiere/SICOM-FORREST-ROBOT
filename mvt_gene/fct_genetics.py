#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import mvt_gene.class_genetics as CG
import parameters as PA

def accouplement(ref_pop) :
        """Fonction d'accouplement de deux individu parmi un population ; renvoi l'enfant"""
        population = ref_pop[:PA.NB_IND_SLT]
        taille=population[0].taille
        a=0
        b=0
        if(len(population) != 1) : 
                while a==b :#on sélectionne deux individu différetn dans la population d'accouplement
                        a=random.randrange(len(population))
                        b=random.randrange(len(population))
        individu1=population[a]
        individu2=population[b]
        coupe=random.randrange(1,taille-1)#on définit la coupe de manière aléatoire
        enfant=CG.individu(taille)
        #print('          coupe',coupe,' individus ', a ,' et ', b)
        #print('                              ',individu1.liste[:coupe])
        #print('                              ',individu2.liste[coupe:])
        enfant.liste = individu1.liste[:coupe] + individu2.liste[coupe:]#l'enfant est généré à partir des 2 individus selectionné coupé à la coupe
        return enfant


def mutation1(individu):
        """Fonction de mutation sur un individu"""
        for i in range(individu.taille) :#on parcours la liste des gènes de l'individu
                        p = random.random()
                        if p < PA.PROBA_MUT :#si le gène doit être muté on génère un nouveau gène aléatoirement 
                                individu.liste[i] = random.randrange(PA.MVT_NB)
def mutation2(individu):
        """fonction de mutation sur un individu

        Cette fonction fait muter un seul gene choisit au hasard"""
        p = random.randrange(PA.SIZE_I) # on choisit la position au hasard dans le genome de l'individu
        individu.liste[p] = random.randrange(PA.MVT_NB)# on remplace le gene choisit par un autre choisit au hasard dans la matrice de mouvement
        
def evaluation(liste):
        """Fonction d evaluation"""
        return random.random()
