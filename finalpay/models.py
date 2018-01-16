from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'finalpay'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_payoff(self):
        n = random.randint(1, 3)
        if n == 1:
            self.payoff = self.participant.vars['payoff1']
        elif n == 2:
            self.payoff = self.participant.vars['payoff2']
        else:
            self.payoff = self.participant.vars['payoff3']

    pass
