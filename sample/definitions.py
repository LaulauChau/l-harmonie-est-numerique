# -*- coding: utf-8 -*-
from collections.abc import Sequence


def calc_frequency(notes: list[str], frequences: list) -> dict[str, int]:
    """Associe chaque note à une fréquence.

    Arg:
        notes: liste de note
        frequences: liste de fréquence en Hz

    Retour:
        Dictionnaire de note et fréquence
    """
    return {note: frequence for note, frequence in zip(notes, frequences)}


def calc_duration(figures: list[str], d0: int) -> dict[str, int]:
    """Associe chaque figure à une durée.

    Arg:
        figure: liste de figure
        d0: durée d'une croche en ms

    Retour:
        Dictionnaire de figure et durée
    """
    figure_duree = {}

    for figure in figures:
        figure_duree.setdefault(figure, d0)
        d0 += d0

    return figure_duree


def read_line_file(f: str, num: int) -> str:
    """Lis le contenue d'une ligne dans une partition.

    Arg:
        f: nom du fichier à lire
        num: numéro de la ligne à lire

    Retour:
        Contenu de la ligne
    """
    with open(f) as fichier:
        for num_ligne in range(num):
            ligne = fichier.readline()

            if not ligne:
                return None

    return ligne


def read_sheet(ligne: str) -> Sequence[list[int], list[str]]:
    """Extrait les fréquences et durées d'une ligne.

    Arg:
        ligne: contenu d'une ligne d'une partition de musique

    Retour:
        Séquence de fréquence et de durée
    """
    note_freq = calc_frequency(notes, frequences)
    fig_duree = calc_duration(figures, d0)
    seq_freq, seq_duree = [], []
    ligne = ligne.split()

    for note in ligne:
        if "p" in note:
            seq_duree[-1] += seq_duree[-1] / 2
        elif "Z" in note:
            seq_freq.append(-1)
            seq_duree.append(-fig_duree[note[-1]])
        else:
            seq_freq.append(note_freq[note[:-1]])
            seq_duree.append(fig_duree[note[-1]])

    return seq_freq, seq_duree


notes = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
frequences = [264, 297, 330, 352, 396, 440, 495]

figures = ["c", "n", "b", "r"]
d0 = 125
