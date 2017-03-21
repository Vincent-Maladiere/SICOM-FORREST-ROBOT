#!/usr/bin/python
# -*- coding: utf-8 -*-
import random,copy
import parameters as PA

class individu(object) :
        """classe de l'individu contenant sa taille, sa série de mouvement et son score"""
        def __init__(self,taille) :
                self.taille = taille
                self.liste = [0 for i in range(taille)]
                self.score = 0

        def random_gen(self) :
                """Génére aléatoirement un individu"""
                for i in range(self.taille) :
                        self.liste[i] = random.randrange(PA.MVT_NB)

        def copy_gen(self, individu) :
                """Génère un individu copy d'un autre individu en s'assurant que les 2 individus soient des objets différent"""
                self.taille = individu.taille
                self.liste = copy.copy(individu.list) #on utilise la fonction copy de la bibliothèque copy qui copie une liste de manière à en faire objet différent mais avec un contenu identique

        def mutation(self,fct_mutation) :
                """Fait la mutation de l'individu selon une probabilité"""
                fct_mutation(self)
                
        def give_score(self,fct_evaluation):
                """ donne le score à un individu à l'aide de sa fonction(fct) d'évaluation """
                self.score = fct_evaluation(self.liste)

        def affiche(self) :
                """ affiche l'individu sous la forme I : [...] || Score : score """
                print('    I: ',self.liste,' || Score: ',self.score)



class generation(object)  :
        """classe representant une generation, elle est definie par sa taille, ses individus et son age"""
        def __init__(self, taille,taille_individu) :
                self.taille = taille
                self.liste = [individu(taille_individu) for i in range(taille) ]
                self.age = 0

        def ran_gen(self) :
                """creation d'une generation compose d individus construit aleatoirement"""
                self.age = 0
                for x in self.liste :
                        x.random_gen()

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

        def next_gene(self,fct_accoupl,fct_mutation) :
                """Construit la génération suivante"""
                self.tri()#tri de la génération
                self.age +=1#on indique que la génération est maintenant la génération suivante
                base_gene = self.copy();#on va utiliser une base copie de notre génération de base
                for i in range(PA.NB_IND_SLT,self.taille) :#on construit les individus pour complété la génération les nb_indiv_selec premier individu étant les individus de la génération précédente sélectionnés 
                        self.liste[i]=fct_accoupl(self.liste)#on génère les enfant qui sont le résultat de l'accouplement des individus sélectionnés
                        self.liste[i].mutation(fct_mutation)#on fait muter cette nouvelle génération
                del base_gene
                return
