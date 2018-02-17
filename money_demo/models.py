from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'money_request'
    players_per_group = 5
    num_rounds = 1


class Subsession(BaseSubsession):


    pass


class Group(BaseGroup):
    def set_payoff(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p5 = self.get_player_by_id(5)

        if p1.choice == p2.choice - 1:
            p1.payoff = p1.choice + 20
            p1.participant.vars['money_pay'] = p1.payoff
        else:
            p1.payoff = p1.choice
            p1.participant.vars['money_pay'] = p1.payoff

        if p2.choice == p1.choice - 1:
            p2.payoff = p2.choice + 20
            p2.participant.vars['money_pay'] = p2.payoff
        else:
            p2.payoff = p2.choice
            p2.participant.vars['money_pay'] = p2.payoff

        if p3.choice == p4.choice - 1:
            p3.payoff = p3.choice + 20
            p3.participant.vars['money_pay'] = p3.payoff
        else:
            p3.payoff = p3.choice
            p3.participant.vars['money_pay'] = p3.payoff

        if p4.choice == p3.choice - 1:
            p4.payoff = p4.choice + 20
            p4.participant.vars['money_pay'] = p4.payoff
        else:
            p4.payoff = p4.choice
            p4.participant.vars['money_pay'] = p4.payoff

        p5.payoff = p5.choice + 20




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
