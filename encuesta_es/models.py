from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'encuesta_es'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    consentimiento = models.StringField(
        choices=['Si', 'No'],
        widget=widgets.RadioSelect)


    dia_nacimiento = models.IntegerField(
        label='¿En qué dìa naciste?',
        min=1, max=31)

    mes_nacimiento = models.IntegerField(
        label='¿En qué mes naciste?',
        min=1, max=12)

    fecha_nacimiento = models.IntegerField(
        label='¿En qué año naciste?',
        min=1900, max=2020)

    genero = models.StringField(
        choices=['Hombre', 'Mujer', 'Otro', 'Prefiero no responder'],
        label='¿Con qué género se identifica?',
        widget=widgets.RadioSelect)

    otro_genero = models.StringField(label='Si desea, especifique su género', blank=True)

    idiomas1 = models.StringField(
        choices=['africaans', 'árabe', 'chapalaa', 'chino', 'croata', 'checo', 'inglés', 'francés', 'hindi', 'isizulu',
                 'japonés', 'coreano', 'polaco', 'quechua', 'ruso', 'serbio', 'setswana', 'shuar', 'eslovaco',
                 'español', 'ucranio', 'huaorani', 'otro', 'Prefiero no responder'],
        label='',
        )

    idiomas2 = models.StringField(
        choices=['africaans', 'árabe', 'chapalaa', 'chino', 'croata', 'checo', 'inglés', 'francés', 'hindi', 'isizulu',
                 'japonés', 'coreano', 'polaco', 'quechua', 'ruso', 'serbio', 'setswana', 'shuar', 'eslovaco',
                 'español', 'ucranio', 'huaorani', 'otro', 'Prefiero no responder'],
        label='',
        blank=True
        )

    idiomas3 = models.StringField(
        choices=['africaans', 'árabe', 'chapalaa', 'chino', 'croata', 'checo', 'inglés', 'francés', 'hindi', 'isizulu',
                 'japonés', 'coreano', 'polaco', 'quechua', 'ruso', 'serbio', 'setswana', 'shuar', 'eslovaco',
                 'español', 'ucranio', 'huaorani', 'otro', 'Prefiero no responder'],
        label='',
        blank=True
        )

    idiomas4 = models.StringField(
        choices=['africaans', 'árabe', 'chapalaa', 'chino', 'croata', 'checo', 'inglés', 'francés', 'hindi', 'isizulu',
                 'japonés', 'coreano', 'polaco', 'quechua', 'ruso', 'serbio', 'setswana', 'shuar', 'eslovaco',
                 'español', 'ucranio', 'huaorani',  'Prefiero no responder'],
        label='',
        blank=True
        )

    especificar_otro1 = models.StringField(label='Por favor, especifique el otro idioma', blank=True)

    especificar_otro2 = models.StringField(label='Por favor, especifique el otro idioma', blank=True)

    especificar_otro3 = models.StringField(label='Por favor, especifique el otro idioma', blank=True)


    masidiomas1 = models.StringField( label='¿Habla  otro  idioma   nativo?',
        choices=['Si', 'No'],  widget=widgets.RadioSelect)

    masidiomas2 = models.StringField( label='¿Habla  otro  idioma   nativo?',
        choices=['Si', 'No'],
        widget=widgets.RadioSelect, blank=True)

    masidiomas3 = models.StringField( label='¿Habla  otro  idioma   nativo?',
        choices=['Si', 'No'],
        widget=widgets.RadioSelect, blank=True)

    dialecto1 = models.StringField(label='')

    dialecto2 = models.StringField(blank=True, label='')

    dialecto3 = models.StringField(blank=True, label='')

    dialecto4 = models.StringField(blank=True, label='')

    pais_nacionalidad = models.StringField(label='',
        choices=['china', 'croacia', 'republica checa', 'ecuador', 'inglaterra', 'francia', 'alemania', 'hungría',
                 'india', 'japón', 'lesoto', 'mexico', 'marruecos', 'peru', 'polonia', 'rusia', 'serbia', 'eslovaquia',
                 'eslovenia', 'sudáfrica', 'corea del sur', 'estados unidos', 'otro', 'Prefiero no responder'],)

    pais_vive = models.StringField(label='',
        choices=['china', 'croacia', 'republica checa', 'ecuador', 'inglaterra', 'francia', 'alemania', 'hungría',
                 'india', 'japón', 'lesoto', 'mexico', 'marruecos', 'peru', 'polonia', 'rusia', 'serbia', 'eslovaquia',
                 'eslovenia', 'sudáfrica', 'corea del sur', 'estados unidos', 'otro', 'Prefiero no responder'],)

    pais_nacio = models.StringField(label='',
        choices=['china', 'croacia', 'republica checa', 'ecuador', 'inglaterra', 'francia', 'alemania', 'hungría',
                 'india', 'japón', 'lesoto', 'mexico', 'marruecos', 'peru', 'polonia', 'rusia', 'serbia', 'eslovaquia',
                 'eslovenia', 'sudáfrica', 'corea del sur', 'estados unidos', 'otro', 'Prefiero no responder'],)


    otro_nacionalidad = models.StringField(blank=True, label='')

    otro_vive = models.StringField(blank=True, label='')

    otro_nacio = models.StringField(blank=True, label='')

    estudiante = models.StringField(
        choices=['Si', 'No', 'Prefiero no responder' ], label='',
        widget=widgets.RadioSelect)

    ocupacion = models.StringField(blank=True, label='')

    nivel_educacion = models.StringField(
        choices=['primaria', 'secundaria', 'algunos clases de la universidad', 'universidad', 'escuela licenciada',
                 'doctorado', 'no está seguro', 'Prefiero no responder'], label='')

    filosofia = models.StringField(
        choices=['ninguno', '1 o 2 cursos', 'más de 2 cursos pero no capacitados en filosofía',
                 'obtener una licenciatura en filosofía', 'tener una licenciatura en filosofía',
                 'obteniendo un degree posgrado en filosofía', 'doctorado en filosofía', 'Prefiero no responder'], label='')

    educacion_padres = models.StringField(
        choices=['primaria', 'secundaria', 'algunos clases de la universidad', 'universidad', 'escuela licenciada',
                 'doctorado', 'no está seguro', 'Prefiero no responder'], label='')

    religion = models.StringField(
        choices=['ninguno', 'católico', 'protestante', 'mormón', 'ortodoxo', 'cristiano', 'judío', 'musulmán - chiíta',
                 'musulmán - sunni', 'hindú', 'budista', 'sintoísmo', 'confuciano', 'daoísta', 'jain', 'sij', 'ateo',
                 'agnóstico', 'otro', 'Prefiero no responder'], label='')

    religion_otro = models.StringField(blank=True, label='')

    importancia_religion = models.StringField(
        choices=['de ningún modo', 'un poco', 'algún tanto', 'bastante', 'muy', 'Prefiero no responder'], label='',
        widget=widgets.RadioSelect)

    actitud_politica  = models.StringField(
        choices=['muy liberal', 'liberal moderado', 'poco liberal', 'ni liberal ni conservador', 'poco conservador',
                 'conservador moderado', 'muy conservado', 'Prefiero no responder'], label='',
        widget=widgets.RadioSelect)

    hermanos = models.IntegerField(
        label='',
        min=0, max=100)

    amigos = models.IntegerField(
        label='',
        min=0, max=100)


