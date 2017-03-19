
# SICOM-FORREST-ROBOT
GRENOBLE-INP PHELMA SICOM

### Prerequisites
Python version 3.3+ is required

## Running the tests

python3 -m test.'pkg'.'test_module'

Lire README.test

test/mvt_gene/test.py : test le fonctionnement des méthodes des class individus et generations
test/mvt_gene/test_convergence.py : test la convergence de l'algorithme genetique en fonction de parametres

## Structure des paquets
### communication
	gére la communication entre la carte raspberry et l'arduino
### imageproc
	gére l'estimation de la distance parcourue en fonction des images prises par la caméra
### config
	contient les fichiers de configuration du robot :
		nb de pins
		degrés de libertés
		etc ....
	et génére la matrice de mouvements
### mvt_gene
	gére les codes génétiques et les mutations

## Paramètres

### Constantes

	MODE_DEBUG = 0
	MODE_SBS = 1
	MODE_NORMAL = 2

### Paramètres utilisateurs

	MODE_FONCTIONNEMENT :

	MODE_TRANSMISSION :

	PARAM_ARDUINO :

	IMAGE_PROC_VEC :


## Authors

Gabriel Destouet,
Pierre Viennet,
Paul-Gauthier Noé,
Nicolas Lepetit,
Vincent Maladière
