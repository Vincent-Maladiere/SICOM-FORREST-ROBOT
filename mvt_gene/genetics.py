import random,time

class individu(object)

  def __init__(self,taille) :
    self.len = taille
    self.list = [0 for i in range(taille)]

  def random_gen(self,mouvements_number) :
      """ Génére aléatoirement un individu"""
      random.seed(time.clock)
      for x in self.list :
          x = random.randrange(mouvements_number)

  def mutation(self,proba_mutation,mouvements_number) :
      """Fait la mutation de l'individu selon une probabilité"""

      random.seed(time.clock)
      for x in self.list :
          p = random.random()
          if p < proba_mutation :
              x = random.randrange(mouvements_number)

  def 
