# Gauge-Invariance

Le code affiche l'évolution d'une config pour une régle donnée. Le temps est représenté de bas en haut.

A priori tous les paramètres utiles à modifier sont dans le main. 
Il faut surement rajouter un plt.imshow() si vous n'êtes pas sur spyder.

Il y'a deux paramètres principaux au début du main:
- T ; le nombre d'étapes temporelles de l'automate à calculer (la largeur spatiale s'adapte automatiquement)
- fusion ; le nombre de fusion à faire avant de plot graphiquement le résultat. Au début je ne faisais pas de fusions et matplotlib commence à faire n'importe quoi
à partir de T=300, i.e. 90 000 petits carrés à plot. Je réalise donc des fusions manuelles pour me rammener à un nombre de petits carrés à dessiner viable.
Chaque fusion remplace un bloc de 9 cellules (3 unités d'espace * 3 unités de temps) par sa valeur binaire (morte ou vivante car les 1 et les 2 ont un role symétrique) moyenne.

IMPORTANT: sans fusion il ne faut pas faire des calculs supérieurs à T=250.
De plus il est conseillé de "rammener" T dans l'intervalle (100-200) avec les fusions, en considérant que chaque fusion divise T par 3.
Exemples de valeurs:
T=150 fusion=0
T=500 fusion=1
T=1000 fusion=2
Au dessus de 9000 mon ordi commence à avoir du mal avec le calcul.


NOTES:
- A partir d'une fusion on obtient une couleur unique.
- On peut modifier la règle utilisée (R ou F) dans l'étape calcul
