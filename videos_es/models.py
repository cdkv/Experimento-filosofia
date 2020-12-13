from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

class Constants(BaseConstants):
    name_in_url = 'exp_es'
    players_per_group = None
    num_rounds = 9

    videomg = 'https://ucla.box.com/v/videostudymg'
    videosk = 'https://ucla.box.com/v/videostudysk'
    videonv = 'https://ucla.box.com/v/videostudynv'
    videoco = 'https://ucla.box.com/v/videostudyco'
    videofb = 'https://ucla.box.com/v/videostudyfb'
    videodo = 'https://ucla.box.com/v/videostudydo'
    videoda = 'https://ucla.box.com/v/videostudypg'
    videopg = 'https://ucla.box.com/v/videostudyda'
    videoin = 'https://ucla.box.com/v/videostudyin'

    videosk_pre1 = 'Pregunta 1: ¿Quién visitó primero a la persona enferma?'
    videosk_pre2 = 'Pregunta 2: ¿Por qué la persona enferma estaba apoyada en el árbol y sosteniendo su cabeza?'
    videosk_pre3 = 'Pregunta 3:¿Por qué el hombre espero tanto para acercarse a la persona enferma?'

    videoco_pre1 = 'Pregunta 1: ¿Qué fue lo que la primera mujer sacó de su caja?'
    videoco_pre2 = 'Pregunta 2: ¿Por qué la primera mujer no le ayudo a la segunda mujer?'
    videoco_pre3 = 'Pregunta 3: ¿Por qué la segunda mujer sacudió su cabeza después de levantar la olla?'

    videodo_pre1 = 'Pregunta 1: ¿El primer hombre estaba parado al principio del video?'
    videodo_pre2 = 'Pregunta 2: ¿Por qué el segundo hombre tomó la madera del primer hombre?'
    videodo_pre3 = 'Pregunta 3: ¿Por qué el segundo hombre solo dejo un pedazo de madera para el primer hombre?'

    videopg_pre1 = 'Pregunta 1: ¿Quién es mejor jugador, el hombre de negro o el hombre de rosado?'
    videopg_pre2 = 'Pregunta 2: ¿Por qué el hombre de negro agitó sus brazos hacia el hombre de gris, después de irse y hablar con el de rosado?'
    videopg_pre3 = 'Pregunta 3: ¿Por qué el hombre de negro no le deja al hombre de gris ver al de rosado?'

    videoda_pre1 = 'Pregunta 1: ¿Qué animal estaba en el árbol?'
    videoda_pre2 = 'Pregunta 2: ¿Por qué la primera mujer paró de hablar y se alejó de la rama?'
    videoda_pre3 = 'Pregunta 3: ¿Por qué la segunda mujer levanto al animal  con un palo después de agredirlo del árbol y golpearlo?'

    videoin_pre1 = 'Pregunta 1: ¿Que dejo caer la segunda mujer cuando entró a la habitación?'
    videoin_pre2 = 'Pregunta 2: ¿Por qué se fue la primera mujer?'
    videoin_pre3 = 'Pregunta 3: ¿Por qué el hombre se puso a gritar? '

    videonv_pre1 = 'Pregunta 1: ¿Qué regalo recibió la mujer?'
    videonv_pre2 = 'Pregunta 2: ¿Por qué el niño les dio los regalos incorrectos?'
    videonv_pre3 = 'Pregunta 3: ¿Por qué el hombre no se inclinó cuando el niño le dio su regalo? '

    videomg_pre1 = 'Pregunta 1: ¿Qué era lo que el segundo hombre tenía con él?'
    videomg_pre2 = 'Pregunta 2: ¿Por qué el primer hombre dio la vuelta a la mujer y la alejó del segundo hombre?'
    videomg_pre3 = 'Pregunta 3: ¿Por qué la mujer continuaba hablando con el Segundo hombre en lugar de irse con el primer hombre de forma inmediata?'

    videofb_pre1 = 'Pregunta 1: ¿Qué dejo el hombre en el árbol?'
    videofb_pre2 = 'Pregunta 2: ¿Por qué el hombre se fue después de quitarse la camiseta? '
    videofb_pre3 = 'Pregunta 3: ¿Por qué el hombre hizo una pausa y miró a su alrededor antes de bañarse?'



    posible_orden_video = {
        0: [videomg, videonv, videoda, videoin, videofb, videosk, videoco, videodo, videopg],
        1: [videonv, videopg, videosk, videomg, videofb, videoda, videodo, videoco, videoin],
        2: [videodo, videosk, videoco, videoin, videofb, videonv, videopg, videoda, videomg],
        3: [videomg, videosk, videonv, videoco, videofb, videodo, videopg, videoda, videoin],
        4: [videomg, videosk, videonv, videoco, videofb, videodo, videopg, videoda, videoin],
        5: [videonv, videodo, videoda, videoco, videoin, videopg, videosk, videomg, videofb],
        6: [videosk, videomg, videodo, videonv, videoda, videoin, videoco, videopg, videofb],
        7: [videoin, videosk, videodo, videoco, videoda, videonv, videomg, videopg, videofb],
        8: [videopg, videosk, videoin, videonv, videoda, videoco, videoco, videomg, videofb],
    }

    posible_orden_pregunta1 = {
        0: ["", "", "", "", "", videosk_pre1, videoco_pre1, videodo_pre1, videopg_pre1],
        1: ["", "", "", "", "", videoda_pre1, videodo_pre1, videoco_pre1, videoin_pre1],
        2: ["", "", "", "", "", videonv_pre1, videopg_pre1, videoda_pre1, videomg_pre1],
        3: ["", "", "", "", "", videodo_pre1, videopg_pre1, videoda_pre1, videoin_pre1],
        4: ["", "", "", "", "", videodo_pre1, videopg_pre1, videoda_pre1, videoin_pre1],
        5: ["", "", "", "", "", videopg_pre1, videosk_pre1, videomg_pre1, videofb_pre1],
        6: ["", "", "", "", "", videoin_pre1, videoco_pre1, videopg_pre1, videofb_pre1],
        7: ["", "", "", "", "", videonv_pre1, videomg_pre1, videopg_pre1, videofb_pre1],
        8: ["", "", "", "", "", videoco_pre1, videoco_pre1, videomg_pre1, videofb_pre1],
    }

    posible_orden_pregunta2 = {
        0: ["", "", "", "", "", videosk_pre2, videoco_pre2, videodo_pre2, videopg_pre2],
        1: ["", "", "", "", "", videoda_pre2, videodo_pre2, videoco_pre2, videoin_pre2],
        2: ["", "", "", "", "", videonv_pre2, videopg_pre2, videoda_pre2, videomg_pre2],
        3: ["", "", "", "", "", videodo_pre2, videopg_pre2, videoda_pre2, videoin_pre2],
        4: ["", "", "", "", "", videodo_pre2, videopg_pre2, videoda_pre2, videoin_pre2],
        5: ["", "", "", "", "", videopg_pre2, videosk_pre2, videomg_pre2, videofb_pre2],
        6: ["", "", "", "", "", videoin_pre2, videoco_pre2, videopg_pre2, videofb_pre2],
        7: ["", "", "", "", "", videonv_pre2, videomg_pre2, videopg_pre2, videofb_pre2],
        8: ["", "", "", "", "", videoco_pre2, videoco_pre2, videomg_pre2, videofb_pre2],
    }

    posible_orden_pregunta3 = {
        0: ["", "", "", "", "", videosk_pre3, videoco_pre3, videodo_pre3, videopg_pre3],
        1: ["", "", "", "", "", videoda_pre3, videodo_pre3, videoco_pre3, videoin_pre3],
        2: ["", "", "", "", "", videonv_pre3, videopg_pre3, videoda_pre3, videomg_pre3],
        3: ["", "", "", "", "", videodo_pre3, videopg_pre3, videoda_pre3, videoin_pre3],
        4: ["", "", "", "", "", videodo_pre3, videopg_pre3, videoda_pre3, videoin_pre3],
        5: ["", "", "", "", "", videopg_pre3, videosk_pre3, videomg_pre3, videofb_pre3],
        6: ["", "", "", "", "", videoin_pre3, videoco_pre3, videopg_pre3, videofb_pre3],
        7: ["", "", "", "", "", videonv_pre3, videomg_pre3, videopg_pre3, videofb_pre3],
        8: ["", "", "", "", "", videoco_pre3, videoco_pre3, videomg_pre3, videofb_pre3],
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.session.get_participants():
                variable = random.randint(0, 7)
                p.vars['aleatorio'] = variable
                diccionario_videos = Constants.posible_orden_video.copy()
                orden_videos = diccionario_videos[variable]
                p.vars['lista_videos'] = orden_videos

                diccionario_pregunta1 = Constants.posible_orden_pregunta1.copy()
                orden_pregunta1 = diccionario_pregunta1[variable]
                p.vars['lista_pregunta1'] = orden_pregunta1

                diccionario_pregunta2 = Constants.posible_orden_pregunta2.copy()
                orden_pregunta2 = diccionario_pregunta2[variable]
                p.vars['lista_pregunta2'] = orden_pregunta2

                diccionario_pregunta3 = Constants.posible_orden_pregunta3.copy()
                orden_pregunta3= diccionario_pregunta3[variable]
                p.vars['lista_pregunta3'] = orden_pregunta3

        else:
            for p in self.session.get_participants():
                p.vars['aleatorio'] = p.vars['aleatorio']


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    dificultad_video = models.StringField(
        choices=['Si', 'No'],
        widget=widgets.RadioSelect, label='')

    vi_des= models.LongStringField(blank=True, label='')

    vi_adicional1 = models.LongStringField(blank=True, label='')

    vi_adicional2 = models.LongStringField(blank=True, label='')

    vi_adicional3 = models.LongStringField(blank=True, label='')

    orden = models.IntegerField()



