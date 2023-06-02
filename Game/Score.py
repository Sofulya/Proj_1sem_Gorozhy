"""подсчет очков"""
class Score:
    def __init__(self):

        self.score = 0
        self.score_up = 1

    def score_upg(self):

        self.score += self.score_up
        print(self.score)