from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'money_req_20'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()

    pass


class Group(BaseGroup):
    def set_payoff(self):
        for p in self.get_players():
            if p.choice == p.other_player().choice - 1:
                p.payoff = p.choice + 10
                p.participant.vars['money_pay'] = p.payoff
            else:
                p.payoff = p.choice
                p.participant.vars['money_pay'] = p.payoff
    pass


class Player(BasePlayer):
    choice = models.IntegerField(
        min=0,
        max=20,
        verbose_name='What amount of money would you request?'
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    pass
