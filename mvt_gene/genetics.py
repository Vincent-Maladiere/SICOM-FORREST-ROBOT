import random,time,copy

class individu(object)
"""classe de l'individu contenant sa taille, sa série de mouvement et son score"""

  def __init__(self,taille) :
    self.taille = taille
    self.liste = [0 for i in range(taille)]
    self.score = 0

  def random_gen(self,mouvements_number) :
      """ Génére aléatoirement un individu"""
      random.seed(time.clock)
      for x in self.liste :
          x = random.randrange(mouvements_number)

  def copy_gen(self, individu) :
      """ Génère un individu copy d'un autre individu"""
      self.taille = individu.taille
      self.liste = copy.copy(individu.list)

  def mutation(self,proba_mutation,mouvements_number) :
      """Fait la mutation de l'individu selon une probabilité"""

      random.seed(time.clock)
      for x in self.liste :
          p = random.random()
          if p < proba_mutation :
              x = random.randrange(mouvements_number)
          






class generation(object)
"""classe de la contenant sa taille, ses individus ,sa veillesse """

  def __init__(self, taille) :
      self.taille = taille ;
      self.liste = [0 for i in range(taille)]
      self.age = 0
  
  def ran_gen(self, mouvements_number, taille_individu) :
      """ generation d'une generation compose de len individu construit aleatoirement"""
      for x in self.liste :
          x = individu(taille_individu)
          x.random_gen(mouvements_numbers)

  def selection(self, nb_invidu_selec) :
      """selection des nb_invidu_selec meilleurs individu parmi une génération"""
      selection = []
      tri_liste=tribulle_individu(self.liste)
      for i in range (self.taille-nb_individu_selec, self.taille) :
          selection.append(tri_liste[i])
      return selection
      
          

  def next_gene(self, nb_indiv_selec, proba_mutation, mouvements_number) :
      """construit la génération suivante"""
      base_gene = self.selection
      next_gene = generation(self.taille)
      next_gene.age = self.age+1
      for i in range(self.taille):
          if i<nb_individu_selec :
              (next_gene.liste)[i]=base_gene[i]
          else :
              (next_gene.liste)[i]=accouplement(base_gene)
      for x in next_gene.liste :
          x.mutation(proba_mutation,mouvements_number)
      
      return next_gene 
      
      
      
      
      

          











def tribulle_individu(liste) :
"""tri bulle sur le score des individus"""
    passage=0
    tri_liste=copy.copy(liste)
    permut = True
    while permut :
        permut = False
        for i in  range(len(liste)-1-passage) :
            if tri_liste[i].score>tri_liste[i+1].score :
                a=tri_liste[i].score
                tri_liste[i].score=tri_liste[i+1].score
                tri_liste[i+1].score=a
                permut=True
        passage=passage+1
    return tri_liste


def accouplement(population) :
"""accouplement de deux individu parmi un population ; renvoi l'enfant"""
    taille=((population.liste)[0]).taille
    a=0
    b=0
    while a=b :
        a=random.randrange(len(population))
        b=random.randrange(len(population))
    individu1=(population.liste)[a]
    individu2=(population.liste)[b]
    coupe=random.randrange(taille)
    enfant=individu(taille)
    for i in range(taille) :
        if i<coupe :
            (enfant.liste)[i]=(invidu1.liste)[i]
        else :
            (enfant.liste)[i]=(invidu2.liste)[i]
        
    return enfant
