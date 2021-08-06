class VoteNotMatchMentionsException(Exception):

    def __init__(self):
        super().__init__()
        print("le vote ne correspond pas aux mentions acceptées")


class VotesNotCounted(Exception):

    def __init__(self):
        super().__init__()
        print("les votes n'ont pas encore été comptabilisés")
