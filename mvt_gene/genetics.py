#!/usr/bin/python
# -*- coding: utf-8 -*-
import random,time,copy

def accouplement(population) :
        """Fonction d'accouplement de deux individu parmi un population ; renvoi l'enfant"""
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
        enfant=individu(taille)
        #print('          coupe',coupe,' individus ', a ,' et ', b)
        #print('                              ',individu1.liste[:coupe])
        #print('                              ',individu2.liste[coupe:])
        enfant.liste = individu1.liste[:coupe] + individu2.liste[coupe:]#l'enfant est généré à partir des 2 individus selectionné coupé à la coupe
        return enfant


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
                """Génère un individu copy d'un autre individu en s'assurant que les 2 individus soient des objets différent"""
                self.taille = individu.taille
                self.liste = copy.copy(individu.list) #on utilise la fonction copy de la bibliothèque copy qui copie une liste de manière à en faire objet différent mais avec un contenu identique

        def mutation(self,proba_mutation,mouvements_number) :
                """Fait la mutation de l'individu selon une probabilité"""
                for i in range(self.taille) :#on parcours la liste des gènes de l'individu
                        p = random.random()
                        if p < proba_mutation :#si le gène doit être muté on génère un nouveau gène aléatoirement 
                                self.liste[i] = random.randrange(mouvements_number)
        def give_score(self,fct):
                """ donne le score à un individu à l'aide de sa fonction(fct) d'évaluation """
                self.score = fct(self.liste)
                return

        def affiche(self) :
                """ affiche l'individu sous la forme I : [...] || Score : score """
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
                """tri la liste d'individu de la génération dans l'ordre de leur score décroissant"""
                self.liste.sort(key=lambda individu : individu.score,reverse=True)
                return

        def copy(self):
                """crée une copie de la génération copie qui n'est pas le meme objet physique mais a le meme contenu ; renvoie cette copie"""
                return copy.deepcopy(self)#deepcopy fait une copie récursive des éléments à l'intérieur de la liste

        def affiche(self) :
                """affiche la génération """
                print( 'Generation : ', self.taille, ' || Age : ',self.age)
                for x in self.liste :
                    x.affiche()

        def next_gene(self, nb_indiv_selec, proba_mutation, mouvements_number,func_accouplement=accouplement) :
                """Construit la génération suivante"""
                self.tri()#tri de la génération
                self.age +=1#on indique que la génération est maintenant la génération suivante
                base_gene = self.copy();#on va utiliser une base copie de notre génération de base
                for i in range(nb_indiv_selec,self.taille) :#on construit les individus pour complété la génération les nb_indiv_selec premier individu étant les individus de la génération précédente sélectionnés 
                        self.liste[i]=func_accouplement(self.liste[:nb_indiv_selec])#on génère les enfant qui sont le résultat de l'accouplement des individus sélectionnés
                        self.liste[i].mutation(proba_mutation,mouvements_number)#on fait muter cette nouvelle génération
                del base_gene
                return



def mutation(liste):
        """Fonction de mutation sur un individu"""
        return liste

def evaluation(liste):
        """Fonction d evaluation"""
        return random.random()
