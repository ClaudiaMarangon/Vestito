from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Rules(Page):
    pass

class vestito(Page):
    form_model = models.Player
    form_fields = ['tshirt', 'hat', 'pants', 'gloves', 'shoes', 'hist']
    def vars_for_template(self):
        return {
            'player1': self.player.id_in_group==1,
            'player2': self.player.id_in_group==2,
            'player3': self.player.id_in_group == 3,
            'player4': self.player.id_in_group == 4,
            'player5': self.player.id_in_group == 5,
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
    vestito,
    ResultsWP,
    Results,
]
