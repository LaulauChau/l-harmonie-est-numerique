# -*- coding: utf-8 -*-
from .context import definitions


def transposition(seq_freq: list[int], k: int) -> list[int]:
    """Transpose une partition.

    Ajoute un entier k à chaque note

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
