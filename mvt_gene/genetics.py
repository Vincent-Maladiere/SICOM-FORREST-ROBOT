#!/usr/bin/python
# -*- coding: utf-8 -*-
import random,time,copy

class individu(object) :
        """classe de l'individu contenant sa taille, sa série de mouvement et son score"""
        def __init__(self,taille) :
                self.taille = taille
                self.liste = [0 for i in range(taille)]
                self.score = 0

        def random_gen(self,mouvements_number) :
                """Génére aléatoirement un individu"""
                for i in range(self.taille) :
                        self.liste[i] = random.randrange(mouvements_number)

        def copy_gen(self, individu) :
                """Génère un individu copy d'un autre individu"""
                self.taille = individu.taille
                self.liste = copy.copy(individu.list)

        def mutation(self,proba_mutation,mouvements_number) :
                """Fait la mutation de l'individu selon une probabilité"""
                for i in range(self.taille) :
                        p = random.random()
                        if p < proba_mutation :
                                self.liste[i] = random.randrange(mouvements_number)
        def give_score(self,fct):
                self.score = fct(self.liste)
                return

        def affiche(self) :
            print('    I: ',self.liste,' || Score: ',self.score)



class generation(object)  :
        """classe representant une generation, elle est definie par sa taille, ses individus et son age"""
        def __init__(self, taille, taille_individu) :
                self.taille = taille
                self.liste = [individu(taille_individu) for i in range(taille) ]
                self.age = 0

        def ran_gen(self, mouvements_number) :
                """creation d'une generation compose d individus construit aleatoirement"""
                self.age = 0
                for x in self.liste :
                        x.random_gen(mouvements_number)

        def tri(self):
                self.liste.sort(key=lambda individu : individu.score,reverse=True)
                return

        def copy(self):
                return copy.deepcopy(self)

        def affiche(self):
                print( 'Generation : ', self.taille, ' || Age : ',self.age)
                for x in self.liste :
                    x.affiche()

        def next_gene(self, nb_indiv_selec, proba_mutation, mouvements_number,func_accouplement) :
                """Construit la génération suivante"""
                self.tri()
                self.age +=1
                base_gene = self.copy();
                for i in range(nb_indiv_selec,self.taille) :
                        self.liste[i]=func_accouplement(base_gene.liste)
                        self.liste[i].mutation(proba_mutation,mouvements_number)
                del base_gene
                return

def accouplement(population) :
        """Fonction daccouplement de deux individu parmi un population ; renvoi l'enfant"""
        taille=population[0].taille
        a=0
        b=0
        while a==b :
                a=random.randrange(len(population))
                b=random.randrange(len(population))
                individu1=population[a]
                individu2=population[b]
        coupe=random.randrange(taille)
        enfant=individu(taille)
        #print('          coupe',coupe,' individus ', a ,' et ', b)
        #print('                              ',individu1.liste[:coupe])
        #print('                              ',individu2.liste[coupe:])
        enfant.liste = individu1.liste[:coupe] + individu2.liste[coupe:] 
        return enfant

def mutation(liste):
        """Fonction de mutation sur un individu"""
        return liste

def evaluation(liste):
        """Fonction d evaluation"""
        return random.random()
