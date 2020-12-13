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

class encuesta (Page):
    form_model = 'player'
    form_fields = ['dia_nacimiento', 'mes_nacimiento', 'fecha_nacimiento',  'genero' ]

class genero (Page):
    form_model = 'player'
    form_fields = [ 'otro_genero', ]

    def is_displayed(self):
        return self.player.genero == "Otro"

class idiomas (Page):
    form_model = 'player'
    form_fields = ['idiomas1', 'masidiomas1' ]

class idiomas_adicional1 (Page):
    form_model = 'player'
    form_fields = ['especificar_otro1', 'idiomas2', 'masidiomas2']

    def is_displayed(self):
        return self.player.idiomas1 == "otro" or self.player.masidiomas1 == "Si"


class idiomas_adicional2(Page):
    form_model = 'player'
    form_fields = ['especificar_otro2', 'idiomas3', 'masidiomas3']

    def is_displayed(self):
        return self.player.idiomas2 == "otro" or self.player.masidiomas2 == "Si"


class idiomas_adicional3(Page):
    form_model = 'player'
    form_fields = ['especificar_otro3', 'idiomas4']

    def is_displayed(self):
        return self.player.idiomas3 == "otro" or self.player.masidiomas3 == "Si"

class dialectos(Page):
    form_model = 'player'
    form_fields = ['dialecto1', 'dialecto2', 'dialecto3', 'dialecto4']

class nacionalidad(Page):
    form_model = 'player'
    form_fields = ['pais_nacionalidad', 'pais_vive', 'pais_nacio']

class otros_nacionalidad(Page):
    form_model = 'player'
    form_fields = ['otro_nacionalidad', 'otro_vive', 'otro_nacio']

    def is_displayed(self):
        return self.player.pais_nacionalidad == "otro" or self.player.pais_vive == "otro" or self.player.pais_nacio == "otro"

class estudia(Page):
    form_model = 'player'
    form_fields = ['estudiante']

class ocupacion(Page):
    form_model = 'player'
    form_fields = ['ocupacion']

    def is_displayed(self):
        return self.player.estudiante == "No"

class educacion(Page):
    form_model = 'player'
    form_fields = ['nivel_educacion', 'filosofia', 'educacion_padres']

class religion(Page):
    form_model = 'player'
    form_fields = ['religion']

class otro_religion(Page):
    form_model = 'player'
    form_fields = ['religion_otro', 'importancia_religion' ]

class politica(Page):
    form_model = 'player'
    form_fields = ['actitud_politica']

class contactos(Page):
    form_model = 'player'
    form_fields = ['hermanos', 'amigos']

page_sequence = [consentimiento, agradecimiento,
                 instrucciones, encuesta, genero,
                 idiomas, idiomas_adicional1, idiomas_adicional2, idiomas_adicional3,
                 dialectos,
                 nacionalidad, otros_nacionalidad,
                 estudia, ocupacion,
                 educacion, religion, otro_religion,
                 politica, contactos
                 ]
