from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Payement_Info(Page):
    def is_displayed(self):
        return self.round_number==1

    form_model = models.Player
    form_fields = ['name', 'surname', 'mail']
    pass

class Rules(Page):

    def is_displayed(self):
        return self.round_number==1

    pass

class Set_Role_Wait_Page(WaitPage):
    def after_all_players_arrive(self):
        pass

class vestito(Page):

    timeout_seconds = 600

    form_model = models.Player
    form_fields = ['tshirt', 'hat', 'pants', 'gloves', 'shoes', 'hist', 'timestamp']
    def vars_for_template(self):
        return {
            'A': self.player.role == 'A',
            'B': self.player.role == 'B',
            'C': self.player.role == 'C',
            'D': self.player.role == 'D',
            'E': self.player.role == 'E',
            'net1': self.group.network == 1,
            'net2': self.group.network == 2,
            'net3': self.group.network == 3,
            'hintts': self.player.hint == 'tshirt',
            'hinth': self.player.hint == 'hat',
            'hintp': self.player.hint == 'pants',
            'hints': self.player.hint == 'shoes',
            'hintg': self.player.hint == 'gloves',
        }


    pass

class ResultsWP(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
    pass


class EndRound(Page):
    def before_next_page(self):
        if self.round_number == 1:
            self.player.participant.vars['payoff_vest'] = 0

        self.player.participant.vars['payoff_vest'] = self.player.participant.vars['payoff_vest'] + self.player.payoff

    pass

class Results(Page):
    def vars_for_template(self):
        return {
            'zero_pay': self.player.partial_pay() < self.group.max(),
            'max_pay': self.group.n_p_max() == 1,
            'max_col': self.player.partial_pay() == self.group.max()
        }
    def before_next_page(self):
        if self.round_number == 1:
            self.player.participant.vars['payoff_vest'] = 0

        self.player.participant.vars['payoff_vest'] = self.player.participant.vars['payoff_vest'] + self.player.payoff

    pass

class NewRound(Page):
    def is_displayed(self):
        return self.round_number > 1

    def before_next_page(self):
        if self.player.id_in_group == 1:
            self.group.set_roles()
            self.group.set_hints()
    pass



class Practice(Page):
    def is_displayed(self):
        return self.round_number == 1
    pass

class Practice2(Page):
    def is_displayed(self):
        return self.round_number==1

    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']

    def q1_error_message(self,value):
        right = (value == 5)
        if not right:
            return 'Question 1 is wrong!'

    def q2_error_message(self,value):
        right = (value == 2)
        if not right:
            return 'Question 2 is wrong!'

    def q3_error_message(self,value):
        right = (value == 2)
        if not right:
            return 'Question 3 is wrong!'

    def q4_error_message(self,value):
        right = (value == 2)
        if not right:
            return 'Question 4 is wrong!'

    def q5_error_message(self,value):
        right = (value == 3)
        if not right:
            return 'Question 5 is wrong!'

    def q6_error_message(self,value):
        right = (value == 1)
        if not right:
            return 'Question 6 is wrong!'

    def q7_error_message(self,value):
        right = (value == 1)
        if not right:
            return 'Question 7 is wrong!'



    pass

class Practice_end(Page):
    def is_displayed(self):
        return self.round_number==1

    def before_next_page(self):
        if self.player.id_in_group == 1:
            self.group.set_roles()
            self.group.set_hints()

    pass

class End(Page):
    def is_displayed(self):
        return self.round_number==4

page_sequence = [
    Payement_Info,
    Rules,
    NewRound,
    Practice,
    Practice2,
    Practice_end,
    Set_Role_Wait_Page,
    vestito,
    ResultsWP,
    EndRound,
    #Results,
    End,
]