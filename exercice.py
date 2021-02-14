#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = number*-1

    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste_nom = []
    for pre in prefixes:
       liste_nom.append(pre + suffixe)

    return liste_nom


def prime_integer_summation() -> int:
    nombre = 6
    nombre_premier = [2, 3, 5]

    while len(nombre_premier) < 100:
        premier = True

        for i in range(2, nombre // 2):
            if (nombre % i == 0):
                premier = False
                break

        if premier:
            nombre_premier.append(nombre)
        nombre += 1

    return sum(nombre_premier)


def factorial(number: int) -> int:
    resultat = 1
    for i in range(number, 0, -1):
        resultat = resultat*i
    return resultat


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
   liste_acceptance = []
   for liste in groups:
       if (len(liste)<=10 and len(liste)>3):
           if 25 in liste :
               liste_acceptance.append(True)
           else:
               for age in liste:
                   if age<18:
                       liste_acceptance.append(False)
                       break
                   elif age>70 and 50 in liste:
                       liste_acceptance.append(False)
       else:
           liste_acceptance.append(False)

   return liste_acceptance

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
