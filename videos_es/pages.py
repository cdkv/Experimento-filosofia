from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class video (Page):
    def vars_for_template(self):
        lista_videos = self.participant.vars['lista_videos'][self.round_number - 1]
        return {'lista_videos': lista_videos}

    def before_next_page(self):
        self.player.orden = self.participant.vars['aleatorio']


class video_des(Page):
    form_model = 'player'
    form_fields = ['vi_des', 'dificultad_video' ]

class video_instrucciones(Page):
    def is_displayed(self):
        return self.round_number == 1

class video_adi(Page):
    form_model = 'player'
    form_fields = ['vi_adicional1']

    def vars_for_template(self):
        lista_pregunta1 = self.participant.vars['lista_pregunta1'][self.round_number - 1]
        return {'lista_pregunta1': lista_pregunta1}

    def is_displayed(self):
        return self.round_number >= 6

class video_adi2(Page):
    form_model = 'player'
    form_fields = ['vi_adicional2']

    def vars_for_template(self):
        lista_pregunta2 = self.participant.vars['lista_pregunta2'][self.round_number - 1]
        return {'lista_pregunta2': lista_pregunta2}

    def is_displayed(self):
        return self.round_number >= 6

class video_adi3(Page):
    form_model = 'player'
    form_fields = ['vi_adicional3' ]

    def vars_for_template(self):
        lista_pregunta3 = self.participant.vars['lista_pregunta3'][self.round_number - 1]
        return {'lista_pregunta3': lista_pregunta3}

    def is_displayed(self):
        return self.round_number >= 6


page_sequence = [video_instrucciones, video, video_des, video_adi, video_adi2, video_adi3]
