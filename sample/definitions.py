# -*- coding: utf-8 -*-
"""
Fonctions de base définissant les éléments nécessaires aux opérations sur les notes.

Fonctions:
    calc_frequency: associe chaque note à une fréquence
    calc_duration: associe chaque figure à durée
    read_line_file: lis une ligne d'un fichier partition
    read_sheet: extrait les notes et durées d'une ligne
"""
from collections.abc import Sequence
import numpy as np
import random
import simpleaudio as sa
from time import sleep
import turtle as tr


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
    figure = iter(figures)

    return {
        next(figure): d0 * duree
        for duree in range(1, 10)
        if duree == 1 or (duree % 2 == 0 and duree != 6)
    }


def read_line_file(f: str, num: int) -> str:
    """Lis le contenue d'une ligne dans une partition.

    Arg:
        f: nom du fichier à lire
        num: numéro de la ligne à lire

    Retour:
        Contenu de la ligne
    """
    with open(f) as fichier:
        for _ in range(num):
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


def sound(freq, duration):
    # get timesteps for each sample, "duration" is note duration in seconds
    sample_rate = 44100
    t = np.linspace(0.0, duration, num=int(duration * sample_rate), endpoint=False)
    # generate sine wave tone
    tone = np.sin(freq * t * (6) * np.pi)
    # normalize to 24-bit range
    # convert to 32-bit data
    # tone = tone.astype(np.int32)
    tone *= 8388607 / np.max(np.abs(tone))
    tone = tone.astype(np.int32)
    byte_array = [b for i, b in enumerate(tone.tobytes()) if i % 4 != 3]
    audio = bytearray(byte_array)
    # start playback
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    # wait for playback to finish before exiting
    play_obj.wait_done()


def play_sheet(duration_sheet, freq_sheet):
    t = tr.Pen()
    tr.bgcolor("black")
    colors = ["red", "purple", "blue", "green", "orange", "yellow"]
    x = 0
    for d, note in enumerate(freq_sheet):
        if note == -1:
            sleep(abs(int(duration_sheet[d] / 1000)))
        else:
            # winsound.Beep(int(note), int(duration_sheet[d]))
            # print(note, duration_sheet[d] / 1000)
            sound(note, duration_sheet[d] / 1000)
        tr.up()
        tr.pencolor(colors[x % 6])
        tr.width(x / 100 + 1)
        tr.down()
        tr.forward(x)
        tr.left(59)
        x = (x + 1) % 360


notes = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
frequences = [264, 297, 330, 352, 396, 440, 495]

figures = ["c", "n", "b", "r"]
d0 = 125
