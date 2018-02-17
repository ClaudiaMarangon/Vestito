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
    players_per_group = 25
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

        if p5.choice == p6.choice - 1:
            p5.payoff = p5.choice + 20
            p5.participant.vars['money_pay'] = p5.payoff
        else:
            p5.payoff = p5.choice
            p5.participant.vars['money_pay'] = p5.payoff

        if p6.choice == p5.choice - 1:
            p6.payoff = p6.choice + 20
            p6.participant.vars['money_pay'] = p6.payoff
        else:
            p6.payoff = p6.choice
            p6.participant.vars['money_pay'] = p6.payoff

        if p7.choice == p8.choice - 1:
            p7.payoff = p7.choice + 20
            p7.participant.vars['money_pay'] = p7.payoff
        else:
            p7.payoff = p7.choice
            p7.participant.vars['money_pay'] = p7.payoff

        if p8.choice == p7.choice - 1:
            p8.payoff = p8.choice + 20
            p8.participant.vars['money_pay'] = p8.payoff
        else:
            p8.payoff = p8.choice
            p8.participant.vars['money_pay'] = p8.payoff

        if p9.choice == p10.choice - 1:
            p9.payoff = p9.choice + 20
            p9.participant.vars['money_pay'] = p9.payoff
        else:
            p9.payoff = p9.choice
            p9.participant.vars['money_pay'] = p9.payoff

        if p10.choice == p9.choice - 1:
            p10.payoff = p10.choice + 20
            p10.participant.vars['money_pay'] = p10.payoff
        else:
            p10.payoff = p10.choice
            p10.participant.vars['money_pay'] = p10.payoff

        if p11.choice == p12.choice - 1:
            p11.payoff = p11.choice + 20
            p11.participant.vars['money_pay'] = p11.payoff
        else:
            p11.payoff = p11.choice
            p11.participant.vars['money_pay'] = p11.payoff

        if p12.choice == p11.choice - 1:
            p12.payoff = p12.choice + 20
            p12.participant.vars['money_pay'] = p12.payoff
        else:
            p12.payoff = p12.choice
            p12.participant.vars['money_pay'] = p12.payoff

        if p13.choice == p14.choice - 1:
            p13.payoff = p13.choice + 20
            p13.participant.vars['money_pay'] = p13.payoff
        else:
            p13.payoff = p13.choice
            p13.participant.vars['money_pay'] = p13.payoff

        if p14.choice == p13.choice - 1:
            p14.payoff = p14.choice + 20
            p14.participant.vars['money_pay'] = p14.payoff
        else:
            p14.payoff = p14.choice
            p14.participant.vars['money_pay'] = p14.payoff

        if p16.choice == p15.choice - 1:
            p16.payoff = p16.choice + 20
            p16.participant.vars['money_pay'] = p16.payoff
        else:
            p16.payoff = p16.choice
            p16.participant.vars['money_pay'] = p16.payoff

        if p15.choice == p16.choice - 1:
            p15.payoff = p15.choice + 20
            p15.participant.vars['money_pay'] = p15.payoff
        else:
            p15.payoff = p15.choice
            p15.participant.vars['money_pay'] = p15.payoff

        if p17.choice == p18.choice - 1:
            p17.payoff = p17.choice + 20
            p17.participant.vars['money_pay'] = p17.payoff
        else:
            p17.payoff = p17.choice
            p17.participant.vars['money_pay'] = p17.payoff

        if p18.choice == p17.choice - 1:
            p18.payoff = p18.choice + 20
            p18.participant.vars['money_pay'] = p18.payoff
        else:
            p18.payoff = p18.choice
            p18.participant.vars['money_pay'] = p18.payoff

        if p19.choice == p20.choice - 1:
            p19.payoff = p19.choice + 20
            p19.participant.vars['money_pay'] = p19.payoff
        else:
            p19.payoff = p19.choice
            p19.participant.vars['money_pay'] = p19.payoff

        if p20.choice == p19.choice - 1:
            p20.payoff = p20.choice + 20
            p20.participant.vars['money_pay'] = p20.payoff
        else:
            p20.payoff = p20.choice
            p20.participant.vars['money_pay'] = p20.payoff

        if p21.choice == p22.choice - 1:
            p21.payoff = p21.choice + 20
            p21.participant.vars['money_pay'] = p21.payoff
        else:
            p21.payoff = p21.choice
            p21.participant.vars['money_pay'] = p21.payoff

        if p22.choice == p21.choice - 1:
            p22.payoff = p22.choice + 20
            p22.participant.vars['money_pay'] = p22.payoff
        else:
            p22.payoff = p22.choice
            p22.participant.vars['money_pay'] = p22.payoff

        if p23.choice == p24.choice - 1:
            p23.payoff = p23.choice + 20
            p23.participant.vars['money_pay'] = p23.payoff
        else:
            p23.payoff = p23.choice
            p23.participant.vars['money_pay'] = p23.payoff

        if p24.choice == p23.choice - 1:
            p24.payoff = p24.choice + 20
            p24.participant.vars['money_pay'] = p24.payoff
        else:
            p24.payoff = p24.choice
            p24.participant.vars['money_pay'] = p24.payoff

        p25.payoff = p25.choice + 20


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
