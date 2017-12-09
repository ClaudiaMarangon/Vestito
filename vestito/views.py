from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Rules(Page):
    def before_next_page(self):
        if self.player.id_in_group == 1:
            self.group.set_roles()
            self.group.set_hints()
    pass

class Set_Role_Wait_Page(WaitPage):
    def after_all_players_arrive(self):
        pass


class Network(Page):
    def vars_for_template(self):
        return {
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

class vestito(Page):
    form_model = models.Player
    form_fields = ['tshirt', 'hat', 'pants', 'gloves', 'shoes', 'hist']
    def vars_for_template(self):
        return {
            'A': self.player.role == 'A',
            'B': self.player.role == 'B',
            'C': self.player.role == 'C',
            'D': self.player.role == 'D',
            'E': self.player.role == 'E',
        }
    pass

class ResultsWP(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
    pass



class Results(Page):
    def vars_for_template(self):
        return {
            'zero_pay': self.player.payoff == Constants.zeropay,
            'max_pay': self.player.payoff == Constants.maxpay,
        }
    pass

class resprova(Page):
    pass

page_sequence = [
    Rules,
    Set_Role_Wait_Page,
    Network,
    vestito,
    ResultsWP,
    Results,
]
