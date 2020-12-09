from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class consentimiento(Page):
    form_model = 'player'
    form_fields = ['consentimiento']

class agradecimiento(Page):
    def is_displayed(self):
        return self.player.consentimiento == "No"

class instrucciones(Page):
    pass

class encuesta1 (Page):
    form_model = 'player'
    form_fields = ['dia_nacimiento', 'mes_nacimiento', 'fecha_nacimiento',  'genero' ]

class genero (Page):
    form_model = 'player'
    form_fields = [ 'otro_genero', ]

    def is_displayed(self):
        return self.player.genero == "Otro"

class idiomas1 (Page):
    form_model = 'player'
    form_fields = ['idiomas1', 'idiomas2', 'idiomas3' ]



class ejer_es (Page):
    pass

class vi_es (Page):
    pass



class vi_pre_es(Page):
    form_model = 'player'
    form_fields = ['vi_1_des', 'dificultad_video' ]



class ejer_0_es (Page):
    form_model = 'player'
    form_fields = ['palabraelegida1',]

page_sequence = [consentimiento, agradecimiento,
                 instrucciones, encuesta1, genero,
                 idiomas1,
                 vi_es, vi_pre_es, ejer_es, ejer_0_es ]
