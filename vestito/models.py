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
    name_in_url = 'vestito'
    players_per_group = 5
    num_rounds = 3
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
        if self.round_number == 1:
            n_list1 = [1, 1, 2, 2, 3]
            for g in self.get_groups():
                g.network = random.choice(n_list1)
                n_list1.remove(g.network)


        if self.round_number == 2:
            n_list2 = [1, 3, 2, 2, 3]
            for g in self.get_groups():
                g.network = random.choice(n_list2)
                n_list2.remove(g.network)

        if self.round_number == 3:
            n_list3 = [1, 1, 3, 2, 3]
            for g in self.get_groups():
                g.network = random.choice(n_list3)
                n_list3.remove(g.network)

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

        if self.tshirt == '':
            n = n + 1

        if self.hat == '':
            n = n + 1

        if self.pants == '':
            n = n + 1

        if self.gloves == '':
            n = n + 1

        if self.shoes == '':
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