from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random, math


author = 'Claudia Marangon'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'vestito_net3'
    players_per_group = 5
    num_rounds = 4
    maxpay = 100
    twopay = 50
    threepay = 33
    fourpay = 25
    fivepay = 20
    zeropay = 0

    color_list = ['red', 'orange', 'yellow', 'blue', 'lightblue',
                  'purple', 'green', 'white', 'black']

class Subsession(BaseSubsession):

    def creating_session(self):

        self.group_randomly()
        for g in self.get_groups():
            g.network = 3


        for g in self.get_groups():
            g.tshirt_col = random.choice(Constants.color_list)
            g.hat_col = random.choice(Constants.color_list)
            g.pants_col = random.choice(Constants.color_list)
            g.shoes_col = random.choice(Constants.color_list)
            g.gloves_col = random.choice(Constants.color_list)

    pass


class Group(BaseGroup):

    def set_roles(self):
        role_list = ['A', 'B', 'C', 'D', 'E']
        for p in self.get_players():
            p.role = random.choice(role_list)
            role_list.remove(p.role)

    def set_hints(self):
        hint_list = ['tshirt', 'hat', 'pants', 'gloves', 'shoes']
        for p in self.get_players():
            p.hint = random.choice(hint_list)
            hint_list.remove(p.hint)

    tshirt_col = models.CharField()
    hat_col = models.CharField()
    pants_col = models.CharField()
    shoes_col = models.CharField()
    gloves_col = models.CharField()

    network = models.PositiveIntegerField()

    def max(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p5 = self.get_player_by_id(5)

        max_pp = max(p1.partial_pay(), p2.partial_pay(), p3.partial_pay(), p4.partial_pay(), p5.partial_pay())
        return max_pp

    def n_p_max(self):
        n_p_m = 0
        for p in self.get_players():
            if p.partial_pay() == self.max():
                n_p_m += 1
        return n_p_m

    def n_p_max_less(self):
        n_p_max_l = self.n_p_max() - 1
        return n_p_max_l

    def set_payoffs(self):

        if self.n_p_max() == 1:
            for p in self.get_players():
                if p.partial_pay() == self.max():
                    p.payoff = Constants.maxpay
                else:
                    p.payoff = Constants.zeropay
        elif self.n_p_max() == 2:
            for p in self.get_players():
                if p.partial_pay() == self.max():
                    p.payoff = Constants.twopay
                else:
                    p.payoff = Constants.zeropay
        elif self.n_p_max() == 3:
            for p in self.get_players():
                if p.partial_pay() == self.max():
                    p.payoff = Constants.threepay
                else:
                    p.payoff = Constants.zeropay
        elif self.n_p_max() == 4:
            for p in self.get_players():
                if p.partial_pay() == self.max():
                    p.payoff = Constants.fourpay
                else:
                    p.payoff = Constants.zeropay
        elif self.n_p_max() == 5:
            for p in self.get_players():
                if p.partial_pay() == self.max():
                    p.payoff = Constants.fivepay

        for p in self.get_players():
            p.payoff = p.payoff + p.partial_pay()

    pass


class Player(BasePlayer):
    q1 = models.IntegerField(
        choices=[
            [1, '5'], [2, '-5'], [3, '20'], [4, '0'], [5, '10']
        ],
        widget=widgets.RadioSelect,
        verbose_name="Question 1. If you were to choose GREEN as the color of the hat, how many tokens would you get?"
    )

    q2 = models.IntegerField(
        choices=[
            [1, '5'], [2, '-5'], [3, '20'], [4, '0'], [5, '10']
        ],
        widget=widgets.RadioSelect,
        verbose_name='Question 2. If you were to choose RED as the color of the hat, how many tokens would you get?'
    )

    q3 = models.IntegerField(
        choices=[
            [1, 'Player E and Player D have two hints each regarding the right colors.'],
            [2, 'Player E and Player D can chat together.'],
            [3, 'Nothing.'],
            [4, 'Player E or Player D already know about the hat.']
        ],
        widget=widgets.RadioSelect,
        verbose_name='Question 3. From the hint concerning the network structure, you see that you are assigned to position C. This means that you will be able to chat with Player D and Player E. Moreover, you can see from the picture that Player D and Player E are connected. What does this imply?'
        )

    q4 = models.IntegerField(
        choices=[
            [1, 'No, Player D does not have any information that you may need.'],
            [2, 'Yes, Player D has certainly received information about a piece of clothing that’s not the hat.'],
            [3, 'Maybe, if Player D has received information about a piece of clothing that’s not the hat.'],
        ],
        widget=widgets.RadioSelect,
        verbose_name='Question 4. Do you think that Player D could have useful information regarding the color combination?'
    )

    q5 = models.IntegerField(
        choices=[
            [1, '40 and 0'], [2, '50 and 33'], [3, '50 and 20'], [4, '50 and 100'], [5, '40 and 33']
        ],
        widget=widgets.RadioSelect,
        verbose_name='Question 5. Suppose that by the end of the round you have collected five hints concerning the colors. Suppose also that you are certain that these five hints are correct, and that all the other four players of the group have these same hints. What is the preliminary score that you expect to receive? What is the bonus score that you expect to receive?'
            )

    q6 = models.IntegerField(
        choices=[
            [1, '40 and 100'], [2, '30 and 100'], [3, '40 and 25'], [4, '40 and 0'], [5, '50 and 20']
        ],
        widget=widgets.RadioSelect,
        verbose_name='Question 6. Suppose that by the end of the round you have collected four hints concerning the colors. Suppose also that you are certain that these four hints are correct, and that none of the other players has as many hints as you have. What is the preliminary score that you expect to receive? What is the bonus score that you expect to receive?'
    )

    q7 = models.IntegerField(
        choices=[
            [1, 'It will be not higher than 40 and no lower than -20.'],
            [2, 'It will be not higher than 30 and no lower than -20.'],
            [3, 'It will be not higher than 40 and no lower than 0.'],
            [4, 'It will be not higher than 30 and no lower than 0.'],
        ],
        widget=widgets.RadioSelect,
        verbose_name='Question 7. Suppose that by the end of the round you have collected four hints concerning the colors. Suppose also that you are not sure whether these hints are correct. What is the preliminary score you expect to receive?'
    )

    name = models.CharField(
        verbose_name="Please enter your First Name:"
    )

    surname = models.CharField(
        verbose_name="Please enter your Last Name:"
    )

    mail = models.CharField(
        verbose_name="Please enter the email adress where you want to receive the payment"
    )
    role = models.CharField()
    hint = models.CharField()

    tshirt = models.CharField(
        blank=True
    )
    hat = models.CharField(
        blank=True
    )
    pants = models.CharField(
        blank=True
    )
    gloves = models.CharField(
        blank=True
    )
    shoes = models.CharField(
        blank=True
    )
    hist = models.TextField(
        blank = True
    )

    timestamp = models.TextField(
        blank=True
    )
    def right_col(self):
        n = 0

        if self.tshirt == self.group.tshirt_col:
            n = n + 1

        if self.hat == self.group.hat_col:
            n = n + 1

        if self.pants == self.group.pants_col:
            n = n + 1

        if self.gloves == self.group.gloves_col:
            n = n + 1

        if self.shoes == self.group.shoes_col:
            n = n + 1

        return n

    def no_col(self):
        n = 0

        if self.tshirt == '' or self.tshirt == 'grey':
            n = n + 1

        if self.hat == '' or self.hat == 'grey':
            n = n + 1

        if self.pants == '' or self.pants == 'grey':
            n = n + 1

        if self.gloves == '' or self.gloves == 'grey':
            n = n + 1

        if self.shoes == '' or self.shoes == 'grey':
            n = n + 1

        return n

    def wrong_col(self):
        n = 5 - self.right_col() - self.no_col()
        return n

    def partial_pay(self):
        pp = 10*self.right_col() - 5 * (5 - self.right_col() - self.no_col())
        return pp

    def chat_nickname(self):
        return 'Player {}'.format(self.role)

    def chat_configs(self):

        if self.group.network == 1:
            configs = []
            for other in self.get_others_in_group():
                if other.id_in_group < self.id_in_group:
                    lower_id, higher_id = other.role, self.role
                else:
                    lower_id, higher_id = self.role, other.role

                if (lower_id == 'A' and higher_id == 'B') or (lower_id == 'B' and higher_id == 'A'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'C' and higher_id == 'D') or (lower_id == 'D' and higher_id == 'C'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'D' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'D'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'C' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'C'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'B' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'B'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

            return configs

        if self.group.network == 2:
            configs = []
            for other in self.get_others_in_group():
                if other.id_in_group < self.id_in_group:
                    lower_id, higher_id = other.role, self.role
                else:
                    lower_id, higher_id = self.role, other.role

                if (lower_id == 'A' and higher_id == 'B') or (lower_id == 'B' and higher_id == 'A'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'A' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'A'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'B' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'B'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'C' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'C'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'D' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'D'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'C' and higher_id == 'D') or (lower_id == 'D' and higher_id == 'C'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

            return configs

        if self.group.network == 3:
            configs = []
            for other in self.get_others_in_group():
                if other.id_in_group < self.id_in_group:
                    lower_id, higher_id = other.role, self.role
                else:
                    lower_id, higher_id = self.role, other.role

                if (lower_id == 'A' and higher_id == 'B') or (lower_id == 'B' and higher_id == 'A'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'B' and higher_id == 'C') or (lower_id == 'C' and higher_id == 'B'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'B' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'B'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'C' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'C'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'D' and higher_id == 'E') or (lower_id == 'E' and higher_id == 'D'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

                if (lower_id == 'C' and higher_id == 'D') or (lower_id == 'D' and higher_id == 'C'):
                    configs.append({
                        'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                        'label': 'Chat with {}'.format(other.chat_nickname())
                    })

            return configs

    pass