# -*- coding: utf-8 -*-

from sample import definitions, ecritures, interface, lectures, transformations


def main():
    """Execute l'action voulut par l'utilisateur.

    Retour:
        None
    """
    while True:
        actions = {
            1: lectures.lecture_systeme,
            2: lectures.lecture_utilisateur,
            3: interface.choix_transfo,
            4: interface.choix_markov,
            5: interface.ajout_fonction,
        }

        choix = interface.choix_utilisateur()

        if choix == 6:
            print("Au revoir !")
            return

        executer = actions.get(choix, interface.choix_incorrect)

        if choix in [3, 4]:
            seq_freq, seq_duree = interface.choix_partition()
        else:
            executer()

        if choix == 3:
            transfo = {1: interface.choix_transpo, 2: interface.choix_inversion}
            exec_transfo = transfo.get(executer(), interface.choix_incorrect)
            transfo_freq, seq_duree = exec_transfo(seq_freq, seq_duree)
        elif choix == 4:
            transfo = {1: interface.choix_markov_1, 2: interface.choix_markov_2}
            exec_transfo = transfo.get(executer(), interface.choix_incorrect)
            len_partition = int(
                input("Quelle est la taille de la nouvelle partition ? ")
            )
            transfo_freq, seq_duree = exec_transfo(seq_freq, seq_duree, len_partition)

        if choix in [3, 4]:
            lecture = int(input("Voulez-vous la lire ? (1/0) "))

            if lecture:
                definitions.play_sheet(seq_duree, transfo_freq)


if __name__ == "__main__":
    main()
