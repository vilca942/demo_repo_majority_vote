"""
Il s'agit d'implémenter le vote majoritaire:
Chaque candidat a une mention entre "Excellent" et "À rejeter".
Exemple de mentions : Excellent [0] Très bien [1] Bien [2] Assez Bien [3] Passable [4] Insuffisant [5] À rejeter [6]
Chaque électeur vote pour une mention de chaque candidat.
La mention majoritaire d'un candidat est calculée sur la médiane et non sur la moyenne :
50 % au moins des votants trouvent la mention majoritaire valable.
Le candidat avec la mention majoritaire la meilleure est mieux classé.
En cas d’égalité de mentions majoritaires : celle ou celui ayant le pourcentage de mentions supérieures
à la mention majoritaire le plus important est le mieux classé.
Le candidat le mieux classé au final est élu.
Dans cette implémentation les votes sont faits au hasard.
"""
from votecontrollerpackage.votecontroller import VoteController


def main():
    vote_controller = VoteController()
    vote_controller.launch_vote()
    vote_controller.print_vote_results()
    vote_controller.reveal_winner()


if __name__ == '__main__':
    main()

