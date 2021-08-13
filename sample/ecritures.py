# -*- coding: utf-8 -*-
"""
Ecriture d'une partition.

Fonctions:
    markov_1: Utilisation des chaines de Markov sur une partition
    markov_2: Utilisation des chaines de Markov sur l'ensemble des partitions
"""
import random
from .context import definitions, transformations, lectures


def markov_1(seq_freq: list[int], len_partition: int) -> list[int]:
    """Utilisation des chaines de Markov sur une partition.

    Arg:
        seq_freq: sequence de frequence de la partition modele
        len_partition: longueur de la nouvelle partition a creer

    Retour:
        Nouvelle partition cree
    """
    successeur = {}

    for note, next_note in zip(seq_freq, seq_freq[1:]):
        successeur.setdefault(note, set()).add(next_note)

    return [
        seq_freq[0],
        *[
            random.choice(list(successeur[random.choice(list(successeur.keys()))]))
            for _ in range(len_partition - 1)
        ],
    ]


def markov_2(len_partition: int) -> list[int]:
    """Utilisation des chaines de Markov sur l'ensemble des partitions.

    Arg:
        len_partition: longueur de la nouvelle partition a creer

    Retour:
        Nouvelle partition cree
    """
    partition = ""
    with open("docs/partitions/partitions.txt") as f:
        for ligne in f.readlines()[1::2]:
            partition += ligne.strip() + " "

    seq_freq, _ = definitions.read_sheet(partition)

    return markov_1(seq_freq, len_partition)
