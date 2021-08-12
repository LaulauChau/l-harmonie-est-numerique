# -*- coding: utf-8 -*-
"""
Interface utilisateur

Fonctions:

"""
from .context import definitions, transformations, lectures, ecritures


def interface() -> None:
    """Permet a l'utilisateur de choisir une action.

    Retour:
        None
    """
    print("Choisissez parmi :")
    print("\t1. Lecture d'une des partitions de la base de donnee\n")
    print("\t2. Lecture d'une de vos partitions\n")
    print("\t3. Transformation d'une partition\n")
    print("\t4. Composition d'une nouvelle partition\n")
    print("\t5. Enrichir la base de donnee avec de nouvelles partitions\n")
    choix = int(input("Choix : "))

    if choix == 1:
        lectures.lecture_systeme()
    elif choix == 2:
        lectures.lecture_utilisateur()
    elif choix == 3:
        print("Choisissez parmi :")
        print("\t1. Transposition\n")
        print("\t2. Inversion\n")
        choix_transfo = int(input("Choix : "))

        print("Choisissez parmi :")
        with open("docs/partitions/partitions.txt") as f:
            for ligne in f.readlines()[::2]:
                print("\t" + ligne.strip()[1::])
        choix_partition = int(input("Choix : "))

        ligne = definitions.read_line_file(
            "docs/partitions/partitions.txt", choix_partition * 2
        )
        seq_freq, duree_seq = definitions.read_sheet(ligne)

        if choix == 1:
            k = int(input("De combien voulez-vous transposer ? "))
            transfo_freq = transformations.transposition(seq_freq, k)
            # afficher transfo_freq
        else:
            transfo_freq = transformations.inversion(seq_freq)
            # afficher transfo_freq

        lecture = int(input("Voulez-vous la lire ? (1/0) "))

        if lecture:
            definitions.play_sheet(duree_seq, transfo_freq)
    elif choix == 4:
        print("Choisissez parmi :")
        print("\t1. Application des chaines de Markov sur une partition\n")
        print(
            "\t2. Application des chaines de Markov sur l'ensemble de la base de donnee\n"
        )
        choix_markov = int(input("Choix : "))

        len_partition = int(input("Quelle est la taille de la nouvelle partition ? "))

        if choix_markov == 1:
            print("Choisissez parmi :")
            with open("docs/partitions/partitions.txt") as f:
                for ligne in f.readlines()[::2]:
                    print("\t" + ligne.strip()[1::])
            choix_partition = int(input("Choix : "))

            ligne = definitions.read_line_file(
                "docs/partitions/partitions.txt", choix_partition * 2
            )
            seq_freq, _ = definitions.read_sheet(ligne)

            transfo_freq = ecritures.markov_1(seq_freq, len_partition)
            # afficher transfo_freq
        else:
            transfo_freq = ecritures.markov_2(len_partition)
            # afficher transfo_freq

        lecture = int(input("Voulez-vous la lire ? (1/0) "))

        if lecture:
            definitions.play_sheet(duree_seq, transfo_freq)
    elif choix == 5:
        pass
    else:
        print("Choix incorrect !\n")
