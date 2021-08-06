from models.votes import Votes
from models.myexception import VotesNotCounted


class Candidat:

    def __init__(self, name: str):
        self.name: str = name
        self.votes = Votes()
        self.major_mention_index: int = None
        self.major_mention_votes: int = None

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        if self.major_mention_index is not None and self.major_mention_votes is not None:
            mention: str = Votes.MENTIONS[self.major_mention_index]
            return self.name + ", mention " + mention + ", avec " + str(self.major_mention_votes)\
                   + " votes pour au moins cette mention"
        return self.name + " : " + str(self.votes)

    def add_vote(self, vote: list):
        self.votes.add_vote(vote)

    def count_votes(self):
        vote_result: list = self.votes.major_mention()
        self.major_mention_index = vote_result[0]
        self.major_mention_votes = vote_result[1]

    def is_winner(self, candidat) -> bool:
        if self.major_mention_index is None or candidat.major_mention_index is None:
            raise VotesNotCounted()
        if self.major_mention_index != candidat.major_mention_index:
            return self.major_mention_index < candidat.major_mention_index
        if self.major_mention_votes is None or self.major_mention_votes is None:
            raise VotesNotCounted()
        return self.major_mention_votes >= candidat.major_mention_votes

    def count_total_votes(self) -> int:
        return self.votes.compute_total_votes()


