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
    name_in_url = 'circle_task_20'
    players_per_group = 2
    num_rounds = 1
    endowmentsqr = float(400)
    ran_numb = random.randrange(1,2)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()

    pass


class Group(BaseGroup):

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if Constants.ran_numb == 1:
            p1.payoff = p1.choice
            p2.payoff = p1.otherpay

        else:
            p1.payoff = p2.otherpay
            p2.payoff = p2.choice

        p1.participant.vars['circlet_payoff'] = p1.payoff
        p2.participant.vars['circlet_payoff'] = p2.payoff
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
