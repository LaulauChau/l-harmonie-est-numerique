# -*- coding: utf-8 -*-
"""
Interface utilisateur

Fonctions:

"""
import random
from .context import definitions, transformations, lectures, ecritures


def interface() -> None:
    """Permet a l'utilisateur de choisir une action.

    Retour:
        None
    """
    print("Choisissez parmi :")
    print("\t1. Lecture d'une des partitions de la base de donnee")
    print("\t2. Lecture d'une de vos partitions")
    print("\t3. Transformation d'une partition")
    print("\t4. Composition d'une nouvelle partition")
    print("\t5. Enrichir la base de donnee avec de nouvelles partitions")
    print("\t6. Quitter")
    choix = int(input("Choix : "))

    if choix == 1:
        lectures.lecture_systeme()
    elif choix == 2:
        lectures.lecture_utilisateur()
    elif choix == 3:
        print("Choisissez parmi :")
        print("\t1. Transposition")
        print("\t2. Inversion")
        choix_transfo = int(input("Choix : "))

        if choix_transfo == 1 or choix_transfo == 2:
            print("Choisissez parmi :")
            with open("docs/partitions/partitions.txt") as f:
                for ligne in f.readlines()[::2]:
                    print("\t" + ligne.strip()[1::])
            choix_partition = int(input("Choix : "))

            ligne = definitions.read_line_file(
                "docs/partitions/partitions.txt", choix_partition * 2
            )
            seq_freq, seq_duree = definitions.read_sheet(ligne)
        else:
            print("Choix incorrect !\n")

        if choix_transfo == 1:
            k = int(input("De combien voulez-vous transposer ? "))
            transfo_freq = transformations.transposition(seq_freq, k)
            print("Partition transposee : ")
            lectures.lecture_transfo(transfo_freq, seq_duree)
        elif choix_transfo == 2:
            transfo_freq = transformations.inversion(seq_freq)
            print("Partition inversee : ")
            lectures.lecture_transfo(transfo_freq, seq_duree)

        if choix_transfo == 1 or choix_transfo == 2:
            lecture = int(input("Voulez-vous la lire ? (1/0) "))

            if lecture:
                definitions.play_sheet(seq_duree, transfo_freq)
    elif choix == 4:
        print("Choisissez parmi :")
        print("\t1. Application des chaines de Markov sur une partition")
        print(
            "\t2. Application des chaines de Markov sur l'ensemble de la base de donnee"
        )
        choix_markov = int(input("Choix : "))

        if choix_markov == 1 or choix_markov == 2:
            len_partition = int(
                input("Quelle est la taille de la nouvelle partition ? ")
            )
        else:
            print("Choix incorrect !\n")

        if choix_markov == 1:
            print("Choisissez parmi :")
            with open("docs/partitions/partitions.txt") as f:
                for ligne in f.readlines()[::2]:
                    print("\t" + ligne.strip()[1::])
            choix_partition = int(input("Choix : "))

            ligne = definitions.read_line_file(
                "docs/partitions/partitions.txt", choix_partition * 2
            )
            seq_freq, seq_duree = definitions.read_sheet(ligne)

            transfo_freq = ecritures.markov_1(seq_freq, len_partition)
            print("Nouvelle partition : ")
            lectures.lecture_transfo(transfo_freq, seq_duree)
        elif choix_markov == 2:
            transfo_freq = ecritures.markov_2(len_partition)
            seq_duree = [
                random.choice(
                    list(
                        definitions.calc_duration(
                            definitions.figures, definitions.d0
                        ).values()
                    )
                )
                for _ in transfo_freq
            ]
            print("Nouvelle partition : ")
            lectures.lecture_transfo(transfo_freq, seq_duree)

        if choix_markov == 1 or choix_markov == 2:
            lecture = int(input("Voulez-vous la lire ? (1/0) "))

            if lecture:
                definitions.play_sheet(seq_duree, transfo_freq)
    elif choix == 5:
        print(
            "Mettez votre fichier partition dans docs/partition et verifier que c'est un fichier texte (.txt)"
        )
        fichier_name = str(input("Entrez le nom de votre fichier : "))
        fichier_name = "docs/partitions/" + fichier_name

        if not os.path.isfile(partition):
            print("Le fichier n'existe pas")
        else:
            ecritures.ajout_partition(fichier_name)
    elif choix == 6:
        print("Au revoir !\n")
        return None
    else:
        print("Choix incorrect !\n")

    recommencer = int(input("Voulez-vous revenir au menu ? (1/0) "))

    if recommencer:
        interface()
    else:
        print("Au revoir !\n")
