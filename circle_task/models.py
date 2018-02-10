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
    players_per_group = 25
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
        p6 = self.get_player_by_id(6)
        p7 = self.get_player_by_id(7)
        p8 = self.get_player_by_id(8)
        p9 = self.get_player_by_id(9)
        p10 = self.get_player_by_id(10)
        p11 = self.get_player_by_id(11)
        p12 = self.get_player_by_id(12)
        p13 = self.get_player_by_id(13)
        p14 = self.get_player_by_id(14)
        p15 = self.get_player_by_id(15)
        p16 = self.get_player_by_id(16)
        p17 = self.get_player_by_id(17)
        p18 = self.get_player_by_id(18)
        p19 = self.get_player_by_id(19)
        p20 = self.get_player_by_id(20)
        p21 = self.get_player_by_id(21)
        p22 = self.get_player_by_id(22)
        p23 = self.get_player_by_id(23)
        p24 = self.get_player_by_id(24)
        p25 = self.get_player_by_id(25)


        if Constants.ran_numb == 1:
            p1.payoff = p1.choice
            p2.payoff = p1.otherpay
            p3.payoff = p3.choice
            p4.payoff = p3.otherpay
            p5.payoff = p5.choice
            p6.payoff = p5.otherpay
            p7.payoff = p7.choice
            p8.payoff = p7.otherpay
            p9.payoff = p9.choice
            p10.payoff = p9.otherpay
            p11.payoff = p11.choice
            p12.payoff = p11.otherpay
            p13.payoff = p13.choice
            p14.payoff = p13.otherpay
            p15.payoff = p15.choice
            p16.payoff = p15.otherpay
            p17.payoff = p17.choice
            p18.payoff = p17.otherpay
            p19.payoff = p19.choice
            p20.payoff = p19.otherpay
            p21.payoff = p21.choice
            p22.payoff = p21.otherpay
            p23.payoff = p23.choice
            p24.payoff = p23.otherpay
            p25.payoff = p25.choice


        else:
            p1.payoff = p2.choice
            p2.payoff = p2.otherpay
            p3.payoff = p4.choice
            p4.payoff = p4.otherpay
            p5.payoff = p6.choice
            p6.payoff = p6.otherpay
            p7.payoff = p8.choice
            p8.payoff = p8.otherpay
            p9.payoff = p10.choice
            p10.payoff = p10.otherpay
            p11.payoff = p12.choice
            p12.payoff = p12.otherpay
            p13.payoff = p14.choice
            p14.payoff = p14.otherpay
            p15.payoff = p16.choice
            p16.payoff = p16.otherpay
            p17.payoff = p18.choice
            p18.payoff = p18.otherpay
            p19.payoff = p20.choice
            p20.payoff = p20.otherpay
            p21.payoff = p22.choice
            p22.payoff = p22.otherpay
            p23.payoff = p24.choice
            p24.payoff = p24.otherpay
            p25.payoff = p25.choice

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
