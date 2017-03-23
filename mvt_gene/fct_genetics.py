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

def mutation3(individu):
        """fonction de mutation sur un individu

        Cette fonction est une evolution de la fonction mutation2, elle fait muter au moins un gene de l'individu les autres genes mutent en f
        onction de la taille du genome ( taille de l'individu ), si on note N la taille de l'individu on aura en moyenne :
           N*(1-(1-1/N)**(N+1)) mutations , pour N = 10 on a ~ 6.8 mutations"""

        P=set()
        
        while P.__len__() != individu.taille : P.add(random.randrange(individu.taille))
        ##mutation certaine ##
        individu.liste[P.pop()] = random.randrange(PA.MVT_NB)

        ##mutation conditionné par la taille de l'individu ##
        n=1
        pos = 0
        p=1-1/individu.taille
        while P.__len__() != 0 :
                pos = P.pop()
                if random.random() > p :
                        individu.liste[pos] = random.randrange(PA.MVT_NB)
                        #n+=1
                p *=p
        #print(n)

def mutation4(individu):
        """Fonction de mutation sur un individu

        variante de mutation3, en limitant par le parametre MUT4_MAX definit dans parameters.py le nombre de mutations
        Pour MUT4_MAX=1, on retrouve mutation2"""
        P=set()
        LEN_P = PA.MUT4_MAX
        while P.__len__() != LEN_P: P.add(random.randrange(individu.taille))
        ##mutation certaine ##
        individu.liste[P.pop()] = random.randrange(PA.MVT_NB)

        ##mutation conditionné par la taille de l'individu ##
        n=1
        pos = 0
        p=1-1/LEN_P
        while P.__len__() != 0 :
                pos = P.pop()
                if random.random() > p :
                        individu.liste[pos] = random.randrange(PA.MVT_NB)
                        #n+=1
                p *=p
        #print(n)

        
def evaluation(liste):
        """Fonction d evaluation"""
        return random.random()
