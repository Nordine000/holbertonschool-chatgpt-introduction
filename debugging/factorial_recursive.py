#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un nombre donné de manière récursive.

    Paramètres:
    n (int): Le nombre entier dont on veut calculer la factorielle.

    Retours:
    int: La factorielle de n.
    """
    if n == 0:
        return 1  # La factorielle de 0 est toujours 1
    else:
        return n * factorial(n-1)  # Appel récursif pour calculer la factorielle

# Récupère l'argument passé en ligne de commande et le convertit en entier
f = factorial(int(sys.argv[1]))

# Affiche le résultat de la factorielle
print(f)