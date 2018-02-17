from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Survey1(Page):
    form_model = models.Player
    form_fields = [ 'age', 'gender', 'economics', 'other', 'game_theory', 'grade_gt']
    pass

class Survey2(Page):
    form_model = models.Player
    form_fields = ['rules', 'others_op', 'polite', 'satisfaction', 'religious', 'tradition', 'planning', 'interest', 'independent', 'govt_inter', 'egoism', 'wealth', 'risk_aversion']
    pass


class Comments(Page):
    form_model = models.Player
    form_fields = ['burglar','process', 'comments']
    pass


page_sequence = [
    Survey1,
    Survey2,
    Comments,
]
