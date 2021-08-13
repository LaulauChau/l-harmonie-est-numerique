# -*- coding: utf-8 -*-
"""
Fonctions permettant a l'utilisateur de choisir et d'effectuer des actions

Fonctions:
    choix_utilisateur: Demande a l'utilisateur de choisir une action a effectuer
    choix_incorrect: 
    
    choix_transfo: Permet a l'utilisateur de choisir parmi l'inversion ou la transposition
    choix_transpo: Transposition d'une partition
    choix_inversion: Inversion d'une partition
    
    choix_markov: Permet a l'utilisateur de choisir d'utiliser markov sur une partition ou l'ensemble de la base de donnee
    choix_markov_1: Application des chaines de Markov sur une partition
    choix_markov_2: Application des chaines de Markov sur l'ensemble de la base de donnee
    
    ajout_fonction: Ajouter des partitions a la base de donnee
"""
import random
from collections.abc import Sequence
from .context import definitions, transformations, lectures, ecritures


def choix_utilisateur() -> int:
    """Demande a l'utilisateur de choisir une action a effectuer.

    Retour:
        Choix de l'utilisateur
    """
    print("\nChoisissez parmi :")
    print("\t1. Lecture d'une des partitions de la base de donnee")
    print("\t2. Lecture d'une de vos partitions")
    print("\t3. Transformation d'une partition")
    print("\t4. Composition d'une nouvelle partition")
    print("\t5. Enrichir la base de donnee avec de nouvelles partitions")
    print("\t6. Quitter")

    return int(input("Choix : "))


def choix_incorrect():
    return print("Choix incorrect !\n")


def choix_transfo():
    """Permet a l'utilisateur de choisir parmi l'inversion ou la transposition.

    Retour:
        Choix de l'utilisateur
    """
    print("Choisissez parmi :")
    print("\t1. Transposition")
    print("\t2. Inversion")

    return int(input("Choix : "))


def choix_transpo(
    seq_freq: list[int], seq_duree: list[float]
) -> Sequence[list[int], list[float]]:
    """Transposition d'une partition.

    Arg:
        seq_freq: sequence de frequence original
        seq_duree: sequence de duree original

    Retour:
        Partition transposee
    """
    k = int(input("De combien voulez-vous transposer ? "))
    transfo_freq = transformations.transposition(seq_freq, k)
    print("Partition transposee : ")
    lectures.lecture_transfo(transfo_freq, seq_duree)

    return transfo_freq, seq_duree


def choix_inversion(
    seq_freq: list[int], seq_duree: list[float]
) -> Sequence[list[int], list[float]]:
    """Inversion d'une partition.

    Arg:
        seq_freq: sequence de frequence original
        seq_duree: sequence de duree original

    Retour:
        Partition inversee
    """
    transfo_freq = transformations.inversion(seq_freq)
    print("Partition inversee : ")
    lectures.lecture_transfo(transfo_freq, seq_duree)

    return transfo_freq, seq_duree


def choix_markov():
    """Permet a l'utilisateur de choisir d'utiliser markov sur une partition ou l'ensemble de la base de donnee.

    Retour:
        Choix de l'utilisateur
    """
    print("Choisissez parmi :")
    print("\t1. Application des chaines de Markov sur une partition")
    print("\t2. Application des chaines de Markov sur l'ensemble de la base de donnee")

    return int(input("Choix : "))


def choix_markov_1(
    seq_freq: list[int], seq_duree: list[float], len_partition: int
) -> Sequence[list[int], list[float]]:
    """Application des chaines de Markov sur une partition.

    Arg:
        seq_freq: sequence de frequence original
        seq_duree: sequence de duree original
        len_partition: taille de la partition a creer

    Retour:
        Nouvelle partition
    """
    transfo_freq = ecritures.markov_1(seq_freq, len_partition)
    print("Nouvelle partition : ")
    lectures.lecture_transfo(transfo_freq, seq_duree)

    return transfo_freq, seq_duree


def choix_markov_2(
    seq_freq: list[int], seq_duree: list[float], len_partition: int
) -> Sequence[list[int], list[float]]:
    """Application des chaines de Markov sur l'ensemble de la base de donnee.

    Arg:
        len_partition: taille de la partition a creer

    Retour:
        Nouvelle partition
    """
    transfo_freq = ecritures.markov_2(len_partition)
    seq_duree = [
        random.choice(
            list(
                definitions.calc_duration(definitions.figures, definitions.d0).values()
            )
        )
        for _ in transfo_freq
    ]
    print("Nouvelle partition : ")
    lectures.lecture_transfo(transfo_freq, seq_duree)

    return transfo_freq, seq_duree


def ajout_fonction():
    """Ajouter des partitions a la base de donnee.

    Retour:
        None
    """
    print(
        "Mettez votre fichier partition dans docs/partition et verifier que c'est un fichier texte (.txt)"
    )
    fichier_name = str(input("Entrez le nom de votre fichier : "))
    fichier_name = "docs/partitions/" + fichier_name

    if not os.path.isfile(partition):
        print("Le fichier n'existe pas")
    else:
        ecritures.ajout_partition(fichier_name)


def choix_partition() -> Sequence[list[int], list[float]]:
    """Demande a l'utilisateur de choisir une partion.

    Retour:
        Sequence de frequences et de durees
    """
    print("Choisissez parmi :")
    with open("docs/partitions/partitions.txt") as f:
        for ligne in f.readlines()[::2]:
            print("\t" + ligne.strip()[1::])
    choix_partition = int(input("Choix : "))

    ligne = definitions.read_line_file(
        "docs/partitions/partitions.txt", choix_partition * 2
    )

    return definitions.read_sheet(ligne)
