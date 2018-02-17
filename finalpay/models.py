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
    payoff_final = models.FloatField()


    def set_payoff(self):
        payoff_fin =  self.participant.vars['payoff_vest'] + self.participant.vars['circlet_payoff'] + self.participant.vars['money_pay']
        if payoff_fin < 100:
            self.payoff_final = 100
        else:
            self.payoff_final = payoff_fin

    pass
