from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class vestito(Page):
    form_model = models.Player
    form_fields = ['tshirt', 'hat', 'pants', 'gloves', 'shoes']
    pass





class Results(Page):
    pass


page_sequence = [
    vestito,
]
