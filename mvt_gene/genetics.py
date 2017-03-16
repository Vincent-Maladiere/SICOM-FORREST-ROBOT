#!/usr/bin/python
# -*- coding: utf-8 -*-
import random,time,copy

class individu(object) :
#classe de l'individu contenant sa taille, sa série de mouvement et son score
	def __init__(self,taille) :
                self.taille = taille
		self.liste = [0 for i in range(taille)]
		self.score = 0

	def random_gen(self,mouvements_number) :
	#Génére aléatoirement un individu
	#random.seed(time.clock)
                for i in range(self.taille) :
                        self.liste[i] = random.randrange(mouvements_number)

	def copy_gen(self, individu) :
	# Génère un individu copy d'un autre individu
		self.taille = individu.taille
		self.liste = copy.copy(individu.list)

        def mutation(self,proba_mutation,mouvements_number) :
	#Fait la mutation de l'individu selon une probabilité
	#random.seed(time.clock)
                for i in range(self.taille) :
                        p = random.random()
                        if p < proba_mutation :
                                self.liste[i] = random.randrange(mouvements_number)

        def affiche(self) :
                print 'l individu a ', self.taille, ' gene qui sont :'
		print self.liste
		print 'son score est de ', self.score



class generation(object)  :
#classe de la contenant sa taille, ses individus ,sa veillesse
	def __init__(self, taille, taille_individu) :
		self.taille = taille
		self.liste = [individu(taille_individu) for i in range(taille) ]
		self.age = 0

	def ran_gen(self, mouvements_number) :
	#generation d'une generation compose de len individu construit aleatoirement
                for x in self.liste :
			x.random_gen(mouvements_number)

	def selection(self, nb_individu_selec):
	#selection des nb_invidu_selec meilleurs individu parmi une génération
		selection = []
		tri_liste=tribulle_individu(self.liste)
		for i in range (self.taille-nb_individu_selec, self.taille) :
			selection.append(tri_liste[i])
		return selection

        def affiche(self):
                print 'c est une generation de ', self.taille, ' individu qui sont :'
                for x in self.liste :
                    x.affiche()
                print 'cette generation est la ', self.age, 'eme generation'

	def next_gene(self, nb_indiv_selec, proba_mutation, mouvements_number) :
	#construit la génération suivante
                base_gene = self.selection(nb_indiv_selec)
                next_gene = generation(self.taille, self.liste[0].taille)
                next_gene.age = self.age+1
		for i in range(self.taille) :
			if i<nb_indiv_selec :
				next_gene.liste[i]=base_gene[i]
			else :
				next_gene.liste[i]=accouplement(base_gene)
                next_gene.liste[i].mutation(proba_mutation,mouvements_number)
		return next_gene





def tribulle_individu(liste) :
#tri bulle sur le score des individus
	passage=0
	tri_liste=copy.copy(liste)
	permut = True
	while permut :
		permut = False
		for i in  range(len(liste)-1-passage) :
			if tri_liste[i].score>tri_liste[i+1].score :
                                permut = True
				a=tri_liste[i]
				tri_liste[i]=tri_liste[i+1]
				tri_liste[i+1]=a
		passage=passage+1
	return tri_liste


def accouplement(population) :
#accouplement de deux individu parmi un population ; renvoi l'enfant
	taille=(population[0]).taille
	a=0
	b=0
	while a==b :
		a=random.randrange(len(population))
		b=random.randrange(len(population))
		individu1=population[a]
		individu2=population[b]
        coupe=random.randrange(taille)
        enfant=individu(taille)
	for i in range(taille) :
		if i<coupe :
			(enfant.liste)[i]=(individu1.liste)[i]
		else :
			(enfant.liste)[i]=(individu2.liste)[i]
	return enfant
