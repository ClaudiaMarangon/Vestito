from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=100
    )
    gender = models.CharField(
        verbose_name='What is your gender?',
        choices=['Female', 'Male'],
        widget=widgets.RadioSelect
    )
    economics = models.CharField(
        verbose_name='What are you studying?',
        choices=['Economics', 'Mathematics', 'Business', 'Law', 'Not studying', 'Other'],
        widget=widgets.RadioSelect
    )
    other = models.CharField(
        verbose_name='If you answered "Other" to the previews question, please specify:',
        blank = True,
    )
    game_theory = models.CharField(
        verbose_name='Did you complete a Game Theory course at your institution?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )
    grade_gt = models.CharField(
        verbose_name='If yes, what grade did you receive?',
        blank = True
    )
    rules = models.PositiveIntegerField(
        verbose_name='This person believes that people should follow rules at all times, even when no-one'
                     'is watching. Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    others_op = models.PositiveIntegerField(
        verbose_name='It is important to this person to always behave well and avoid doing anything people say is wrong.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    polite = models.PositiveIntegerField(
        verbose_name='It is important for this person to be polite to other people all the time and never annoy others.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    satisfaction = models.PositiveIntegerField(
        verbose_name='This person believes that people should be satisfied with what they have.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    religious = models.PositiveIntegerField(
        verbose_name='Religious belief is important to this person and tries hard to do what religion requires.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    tradition = models.PositiveIntegerField(
        verbose_name='This person thinks it is best to do things in traditional ways and keep up the customs he has learned.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    planning = models.PositiveIntegerField(
        verbose_name='It is important to this person to make own plans and decide what to do.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    interest = models.PositiveIntegerField(
        verbose_name='This person thinks it is important to be interested in things and try to understand all sorts of things.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    independent = models.PositiveIntegerField(
        verbose_name='It is important to this person to be independent and rely on himself/herself.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    govt_inter = models.PositiveIntegerField(
        verbose_name='This person thinks it is important that Governments share the wealth in our society as equally as possible.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    egoism = models.PositiveIntegerField(
        verbose_name='This person thinks that it is natural to want to earn more money, even if it means that other people will lose money as a result.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    wealth = models.PositiveIntegerField(
        verbose_name='This person thinks it is important to be rich, to have a lot of money and expansive things.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    risk_aversion = models.PositiveIntegerField(
        verbose_name='Please select the description that sounds most similar to you',
        choices=[
            [1, 'I am very willing to take risks'],
            [2, 'I am somewhat willing to take risks'],
            [3, 'I am somewhat against taking risks'],
            [4, 'I am very much against taking risks'],
        ],
        widget = widgets.RadioSelect
    )

    process = models.TextField(
        verbose_name = '[Max. 500 characters open-text box - must not be left blank]',
        max_length = 500
    )

    comments = models.TextField(
        verbose_name='[Max. 500 characters open-text box - can be left blank]',
        blank = True,
        max_length=500
    )

    burglar = models.TextField(
        verbose_name = 'Why did the burglar do that?'
    )
    pass
