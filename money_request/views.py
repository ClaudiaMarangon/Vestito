from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = models.Player
    form_fields = ['choice']
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class Results(Page):
    pass


page_sequence = [
    Instructions,
    ResultsWaitPage,
    Results
]
