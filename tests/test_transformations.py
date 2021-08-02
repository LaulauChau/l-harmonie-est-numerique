# -*- coding: utf-8 -*-
"""
Test des fonctions du modules sample/transformations
"""
from .context import transformations


def test_transformation():
    freq_seq = [396, -1, 396, 440, 396, 264]
    transpo_freq_seq = [330, -1, 330, 352, 330, 440]

    assert transformations.transposition(freq_seq, 5) == transpo_freq_seq


def test_inversion():
    freq_seq = [396, -1, 396, 440, 396, 264]
    inv_freq_seq = [352, -1, 352, 330, 352, 264]

    assert transformations.inversion(freq_seq) == inv_freq_seq
