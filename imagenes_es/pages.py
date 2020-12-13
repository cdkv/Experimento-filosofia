from otree.api import Currency as c, currency_range
import random

from ._builtin import Page, WaitPage
from .models import Constants

class segundaactividad (Page):
    def is_displayed(self):
        return self.round_number == 1

class imagen (Page):
    form_model = 'player'
    form_fields = ['palabraelegida']

    def palabraelegida_choices(self):
        choices = self.participant.vars[(str(self.round_number))]
        random.shuffle(choices)
        return choices

    def vars_for_template(self):
        image = self.participant.vars['images'][self.round_number - 1]
        palabra1 = self.participant.vars[(str(self.round_number))][0]
        palabra2 = self.participant.vars[(str(self.round_number))][1]
        palabra3 = self.participant.vars[(str(self.round_number))][2]
        palabra4 = self.participant.vars[(str(self.round_number))][3]

        return {'img_to_show': image,
                'palabra1': palabra1,
                'palabra2': palabra2,
                'palabra3': palabra3,
                'palabra4': palabra4}

    def before_next_page(self):
        self.player.guardar_lista = str(self.participant.vars[(str(self.round_number))])

page_sequence = [segundaactividad, imagen ]
