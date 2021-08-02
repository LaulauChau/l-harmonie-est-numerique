# -*- coding: utf-8 -*-
"""
Transformation d'une partition.

Fonctions:
    transposition: ajoute un entier k à chaque note
    inversion: inverse une ligne
"""
from .context import definitions


def transposition(seq_freq: list[int], k: int) -> list[int]:
    """Transpose une partition.

    Ajoute un entier k à chaque notgite

    Arg:
        seq_freq: séquence de fréquence
        k: entier à ajouter à chaque note

    Retour:
        Séquence de fréquence transposée
    """
    note_freq = definitions.calc_frequency(definitions.notes, definitions.frequences)
    note_freq_valeur = list(note_freq.values())
    freq_transpo = []

    for note in seq_freq:
        if note == -1:
            freq_transpo.append(-1)
        else:
            note_transpo = (note_freq_valeur.index(note) + k) % len(note_freq_valeur)
            freq_transpo.append(note_freq_valeur[note_transpo])

    return freq_transpo


def inversion(seq_freq: list[int]) -> list[int]:
    """Inverse une partition.

    Arg:
        seq_freq: séquence de fréquence

    Retour:
        Séquence de fréquence inversée
    """
    note_freq = definitions.calc_frequency(definitions.notes, definitions.frequences)
    note_freq_valeur = list(note_freq.values())
    freq_inv = []

    for note in seq_freq:
        if note == -1:
            freq_inv.append(-1)
        else:
            note_inv = list(note_freq.values())[-note_freq_valeur.index(note)]
            freq_inv.append(note_inv)

    return freq_inv
