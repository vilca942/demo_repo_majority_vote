from models.myexception import VoteNotMatchMentionsException
from random import randint


class Votes:
    MENTIONS = [
        "Excellent",
        "Très bien",
        "Bien",
        "Assez Bien",
        "Passable",
        "Insuffisant",
        "A rejeter"
    ]

    def init_votes_list(votes_list: list):
        for i in range(len(Votes.MENTIONS)):
            votes_list.append(0)

    def __init__(self):
        self.votes_list: list[int] = []
        Votes.init_votes_list(self.votes_list)

    def __str__(self) -> str:
        return self.votes_list.__str__()

    def get_votes_list(self) -> list:
        return self.votes_list

    def add_vote(self, vote: list):
        if not len(vote) == len(self.votes_list):
            raise VoteNotMatchMentionsException()
        for i in range(len(vote)):
            self.votes_list[i] += vote[i]

    def get_random_vote() -> list:
        vote = []
        Votes.init_votes_list(vote)
        random_index = randint(0, len(Votes.MENTIONS) - 1)
        vote[random_index] = 1
        return vote

    def compute_total_votes(self) -> int:
        total_votes: int = 0
        for i in range(len(Votes.MENTIONS)):
            total_votes += self.votes_list[i]
        return total_votes

    def major_mention(self) -> list:
        """
        La méthode renvoie l'indice de la mention majoritaire et le nombre de votes pour une mention
        supérieure ou égale à la mention majoritaire.
        """
        total_votes = self.compute_total_votes()
        mediane_votes = (total_votes + total_votes % 2) / 2  # calcul pour la médiane
        major_mention_index = 0
        current_votes = self.votes_list[0]
        while current_votes < mediane_votes:
            major_mention_index += 1
            current_votes += self.votes_list[major_mention_index]
        return [major_mention_index, current_votes]

