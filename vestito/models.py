from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random, math


author = 'Claudia Marangon'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'vestito'
    players_per_group = 5
    num_rounds = 1
    maxpay = 100
    twopay = 50
    threepay = 33
    fourpay = 25
    fivepay = 20
    zeropay = 0
    color_list = ['red', 'orange', 'yellow', 'blue', 'lightblue',
                  'purple', 'green', 'white', 'grey', 'black']

class Subsession(BaseSubsession):

    def creating_session(self):
        for g in self.get_groups():
            g.tshirt_col = random.choice(Constants.color_list)
            g.hat_col = random.choice(Constants.color_list)
            g.pants_col = random.choice(Constants.color_list)
            g.shoes_col = random.choice(Constants.color_list)
            g.gloves_col = random.choice(Constants.color_list)

    pass


class Group(BaseGroup):

    tshirt_col = models.CharField()
    hat_col = models.CharField()
    pants_col = models.CharField()
    shoes_col = models.CharField()
    gloves_col = models.CharField()


    def max(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p5 = self.get_player_by_id(5)

        max_right = max(p1.right_col(), p2.right_col(), p3.right_col(), p4.right_col(), p5.right_col())
        return max_right

    def n_p_max(self):

        n_p_m = 0

        for p in self.get_players():
            if p.right_col() == self.max():
                n_p_m += 1

        return n_p_m

    def n_p_max_less(self):
        n_p_max_l = self.n_p_max() - 1
        return n_p_max_l

    def set_payoffs(self):

        self.n_p_max_less = self.n_p_max() - 1

        if self.n_p_max() == 1:
            for p in self.get_players():
                if p.right_col() == self.max():
                    p.payoff = Constants.maxpay
                else:
                    p.payoff = Constants.zeropay

        if self.n_p_max() == 2:
            for p in self.get_players():
                if p.right_col() == self.max():
                    p.payoff = Constants.twopay
                else:
                    p.payoff = Constants.zeropay

        if self.n_p_max == 3:
            for p in self.get_players():
                if p.right_col() == self.max():
                    p.payoff = Constants.threepay
                else:
                    p.payoff = Constants.zeropay

        if self.n_p_max == 4:
            for p in self.get_players():
                if p.right_col() == self.max():
                    p.payoff = Constants.fourpay
                else:
                    p.payoff = Constants.zeropay

        if self.n_p_max == 5:
            for p in self.get_players():
                if p.right_col() == self.max():
                    p.payoff = Constants.fivepay

    pass


class Player(BasePlayer):
    tshirt = models.CharField()
    hat = models.CharField()
    pants = models.CharField()
    gloves = models.CharField()
    shoes = models.CharField()
    hist = models.TextField()



    def right_col(self):
        n = 0

        if self.tshirt == self.group.tshirt_col:
            n = 1

        if self.hat == self.group.hat_col:
            n = n + 1

        if self.pants == self.group.pants_col:
            n = n + 1

        if self.gloves == self.group.gloves_col:
            n = n + 1

        if self.shoes == self.group.shoes_col:
            n = n + 1

        return n
    pass
