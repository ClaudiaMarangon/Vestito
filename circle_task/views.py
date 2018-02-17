from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




class Choice(Page):
    form_model = models.Player
    form_fields = ['choice', 'otherpay']
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
    pass

class Results(Page):
    def vars_for_template(self):
        return {
            'P_choice': self.player.payoff == self.player.choice,
        }
    pass


page_sequence = [
    Choice,
    ResultsWaitPage,
    #Results,
]
