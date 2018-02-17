from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math
import random

author = 'Claudia Marangon'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'circle_task'
    players_per_group = 5
    num_rounds = 1
    endowmentsqr = float(400)
    ran_numb = random.randrange(1,2)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p5 = self.get_player_by_id(5)


        if Constants.ran_numb == 1:
            p1.payoff = p1.choice
            p2.payoff = p1.otherpay
            p3.payoff = p3.choice
            p4.payoff = p3.otherpay
            p5.payoff = p5.choice

        else:
            p1.payoff = p2.choice
            p2.payoff = p2.otherpay
            p3.payoff = p4.choice
            p4.payoff = p4.otherpay
            p5.payoff = p5.choice


        for p in self.get_players():
            p.participant.vars['circlet_payoff'] = p.payoff
    pass


class Player(BasePlayer):
    choice = models.FloatField()
    otherpay = models.FloatField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def partner_choice(self):
        return self.other_player().choice

    def partner_yourp(self):
        return self.other_player().otherpay


    pass
