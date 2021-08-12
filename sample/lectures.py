# -*- coding: utf-8 -*-
"""
Lecture d'une partition.

Fonctions:
    lecture_systeme: lecture du fichier partition existant dans le dossier
    lecture_utilisateur: lecture du fichier partition fourni par l'utilisateur
"""
import os.path
from .context import definitions, transformations


def lecture_systeme(nom_partition: str = "docs/partitions/partitions.txt") -> None:
    """Lis une partition dans le fichier.

    Arg:
        nom_partition: nom du fichier contenant les partitions

    Retour:
        None
    """
    nb_ligne = 0

    print("Choisissez une partition parmi : ")

    with open(nom_partition) as f:
        for ligne in f.readlines()[::2]:
            print("\t" + ligne.strip()[1:])
            nb_ligne += 1

    num = int(input("Choix : "))

    if num > nb_ligne:
        print("Choix incorrect !")
    else:
        ligne = definitions.read_line_file(nom_partition, num * 2)
        seq_freq, seq_duree = definitions.read_sheet(ligne)
        definitions.play_sheet(seq_duree, seq_freq)


def lecture_utilisateur():
    """Lis une partition dans un fichier fournis par l'utilisateur.

    Arg:
        None

    Retour:
        None
    """
    print(
        "Mettez votre fichier partition dans docs/partition et verifier que c'est un fichier texte (.txt)"
    )
    partition = str(input("Entrez le nom de votre partition : "))
    partition = "docs/partitions/" + partition

    if not os.path.isfile(partition):
        print("Le fichier n'existe pas")
    else:
        lecture_systeme(partition)
