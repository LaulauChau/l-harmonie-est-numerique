# -*- coding: utf-8 -*-
from .context import definitions


def test_calc_frequency():
    note_freq = {
        "DO": 264,
        "RE": 297,
        "MI": 330,
        "FA": 352,
        "SOL": 396,
        "LA": 440,
        "SI": 495,
    }

    assert type(note_freq) == type(
        definitions.calc_frequency(definitions.notes, definitions.frequences)
    )
    assert note_freq == definitions.calc_frequency(
        definitions.notes, definitions.frequences
    )


def test_calc_duration():
    fig_duree = {"c": 125, "n": 250, "b": 500, "r": 1000}

    assert type(fig_duree) == type(
        definitions.calc_duration(definitions.figures, definitions.d0)
    )
    assert fig_duree == definitions.calc_duration(definitions.figures, definitions.d0)


def test_read_line_file():
    ligne_3 = "#2 Au claire de la lune\n"
    ligne_14 = "SIb LAn SOLb SOLn LAn SOLn LAn SIb SOLn SIb LAn SOLb SOLn LAn SIn LAn SOLb REn REn SIn REn REb REn REn SIn REn REb SIn SIn DOn REn LAb SIn SIn DOn REn LAb\n"
    ligne_22 = "MIn DOn MIn DOn REc MIc FAc MIn REc SOLn MIn DOn MIn DOn MIn DOn REc MIc FAc MIn REc SOLn DOn\n"
    ligne_19 = "#10 Le bon roi Dagobert\n"

    assert type(definitions.read_line_file("docs/partitions/partitions.txt", 1)) == str
    assert definitions.read_line_file("docs/partitions/partitions.txt", 3) == ligne_3
    assert definitions.read_line_file("docs/partitions/partitions.txt", 14) == ligne_14
    assert definitions.read_line_file("docs/partitions/partitions.txt", 22) == ligne_22
    assert definitions.read_line_file("docs/partitions/partitions.txt", 19) == ligne_19


def test_read_sheet():
    ligne = "SOLc p Zc SOLn LAn SOLn DOn"
    freq_seq = [396, -1, 396, 440, 396, 264]
    duration_seq = [187.5, -125, 250, 250, 250, 250]

    assert definitions.read_sheet(ligne) == (freq_seq, duration_seq)
