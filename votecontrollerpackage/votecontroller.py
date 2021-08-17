from models.candidat import Candidat
from models.votes import Votes


class VoteController:
    CANDIDATES = {
        "candidat1": "Candidat 1",
        "candidat2": "Candidat 2",
        "candidat3": "Candidat 3",
        "candidat4": "Candidat 4",
        "candidat5": "Candidat 5",
        "candidat6": "Candidat 6"
    }

    VOTER_NUMBER = 100000

    def __init__(self):
        self.candidats_list = []
        for name_key in self.CANDIDATES:
            new_candidat = Candidat(self.CANDIDATES[name_key])
            self.candidats_list.append(new_candidat)

    def launch_vote(self):
        for i in range(self.VOTER_NUMBER):
            for candidat in self.candidats_list:
                random_vote = Votes.get_random_vote()
                candidat.add_vote(random_vote)

    def print_vote_results(self):
        for candidat in self.candidats_list:
            candidat.count_votes()
            print(str(candidat))

    def reveal_winner(self):
        winner = self.candidats_list[0]
        for candidat in self.candidats_list:
            if candidat.is_winner(winner):
                winner = candidat
        print()
        print("Le gagnant est " + str(winner))




