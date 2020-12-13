from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'imagenes_es'
    players_per_group = None
    num_rounds = 37

    imgs = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg',
            '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg',
            '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg',
            '31.jpg', '32.jpg', '33.jpg', '34.jpg', '35.jpg', '36.jpg', '37.jpg',
            ]

    palabras_imagen1 = ['celoso', 'en pánico', 'arrogante', 'lleno de odio']
    palabras_imagen2 = ['juguetón', 'reconfortante', 'irritado', 'aburrido']
    palabras_imagen3 = ['aterrorizado', 'molesto', 'arrogante', 'enfadado']
    palabras_imagen4 = ['bromista', 'agobiada', 'deseo', 'convencida']
    palabras_imagen5 = ['bromista', 'insistente', 'entretenido', 'relajado']
    palabras_imagen6 = ['irritado', 'sarcástico', 'preocupado', 'amistoso']
    palabras_imagen7 = ['asustada', 'fantasiosa', 'impaciente', 'alarmada']
    palabras_imagen8 = ['arrepentido', 'amistoso', 'intranquilo', 'decaído']
    palabras_imagen9 = ['abatido', 'aliviado', 'tímido', 'entusiasmado']
    palabras_imagen10 = ['enfadada', 'hostil', 'horrorizada', 'angustiada']
    palabras_imagen11 = ['prudente', 'insistente', 'aburrido', 'asustado']
    palabras_imagen12 = ['aterrorizado', 'entretenido', 'arrepentido', 'seductor']
    palabras_imagen13 = ['indiferente', 'abochornado', 'escéptico', 'decaído']
    palabras_imagen14 = ['decidido', 'expectante', 'amenazante', 'tímido']
    palabras_imagen15 = ['irritado', 'decepcionado', 'deprimido', 'acusante']
    palabras_imagen16 = ['abstraída', 'agobiada', 'alentadora', 'entretenida']
    palabras_imagen17 = ['irritado', 'considerado', 'alentador', 'compasivo']
    palabras_imagen18 = ['insegura', 'afectuosa', 'juguetona', 'asustada']
    palabras_imagen19 = ['decidida', 'entretenida', 'asustada', 'aburrida']
    palabras_imagen20 = ['arrogante', 'agradecida', 'sarcástica', 'vacilante']
    palabras_imagen21 = ['imponente', 'amistoso', 'culpable', 'horrorizado']
    palabras_imagen22 = ['abochornada', 'fantasiosa', 'confundida', 'en pánico']
    palabras_imagen23 = ['angustiada', 'agradecida', 'insistente', 'suplicante']
    palabras_imagen24 = ['satisfecho', 'arrepentido', 'desafiante', 'curioso']
    palabras_imagen25 = ['abstraído', 'irritado', 'entusiasmado', 'hostil']
    palabras_imagen26 = ['en pánico', 'incrédula', 'abatida', 'interesada']
    palabras_imagen27 = ['alarmado', 'tímido', 'hostil', 'ansioso']
    palabras_imagen28 = ['bromista', 'prudente', 'arrogante', 'tranquilizadora']
    palabras_imagen29 = ['interesada', 'bromista', 'afectuosa', 'satisfecha']
    palabras_imagen30 = ['impaciente', 'asustada', 'irritada', 'reflexiva']
    palabras_imagen31 = ['agradecida', 'seductora', 'hostil', 'decepcionada']
    palabras_imagen32 = ['avergonzada', 'segura', 'bromista', 'decaída']
    palabras_imagen33 = ['serio', 'avergonzado', 'desconcertado', 'alarmado']
    palabras_imagen34 = ['abochornado', 'culpable', 'fantasioso', 'preocupado']
    palabras_imagen35 = ['asustada', 'desconcertada', 'recelosa', 'aterrorizada']
    palabras_imagen36 = ['perpleja', 'nerviosa', 'insistente', 'abstraída']
    palabras_imagen37 = ['avergonzado', 'nervioso', 'desconfiado', 'indeciso']

    diccionario_palabras = {
        0: palabras_imagen1,
        1: palabras_imagen2,
        2: palabras_imagen3,
        3: palabras_imagen4,
        4: palabras_imagen5,
        5: palabras_imagen6,
        6: palabras_imagen7,
        7: palabras_imagen8,
        8: palabras_imagen9,
        9: palabras_imagen10,
        10: palabras_imagen11,
        11: palabras_imagen12,
        12: palabras_imagen13,
        13: palabras_imagen14,
        14: palabras_imagen15,
        15: palabras_imagen16,
        16: palabras_imagen17,
        17: palabras_imagen18,
        18: palabras_imagen19,
        19: palabras_imagen20,
        20: palabras_imagen21,
        21: palabras_imagen22,
        22: palabras_imagen23,
        23: palabras_imagen24,
        24: palabras_imagen25,
        25: palabras_imagen26,
        26: palabras_imagen27,
        27: palabras_imagen28,
        28: palabras_imagen29,
        29: palabras_imagen30,
        30: palabras_imagen31,
        31: palabras_imagen32,
        32: palabras_imagen33,
        33: palabras_imagen34,
        34: palabras_imagen35,
        35: palabras_imagen36,
        36: palabras_imagen37,
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.session.get_participants():
            imgs = Constants.imgs.copy()
            p.vars['images'] = imgs
            diccionario_palabras = Constants.diccionario_palabras.copy()

            palabras_para_imagen1 = diccionario_palabras[0]
            palabras_para_imagen2 = diccionario_palabras[1]
            palabras_para_imagen3 = diccionario_palabras[2]
            palabras_para_imagen4 = diccionario_palabras[3]
            palabras_para_imagen5 = diccionario_palabras[4]
            palabras_para_imagen6 = diccionario_palabras[5]
            palabras_para_imagen7 = diccionario_palabras[6]
            palabras_para_imagen8 = diccionario_palabras[7]
            palabras_para_imagen9 = diccionario_palabras[8]
            palabras_para_imagen10 = diccionario_palabras[9]
            palabras_para_imagen11 = diccionario_palabras[10]
            palabras_para_imagen12 = diccionario_palabras[11]
            palabras_para_imagen13 = diccionario_palabras[12]
            palabras_para_imagen14 = diccionario_palabras[13]
            palabras_para_imagen15 = diccionario_palabras[14]
            palabras_para_imagen16 = diccionario_palabras[15]
            palabras_para_imagen17 = diccionario_palabras[16]
            palabras_para_imagen18 = diccionario_palabras[17]
            palabras_para_imagen19 = diccionario_palabras[18]
            palabras_para_imagen20 = diccionario_palabras[19]
            palabras_para_imagen21 = diccionario_palabras[20]
            palabras_para_imagen22 = diccionario_palabras[21]
            palabras_para_imagen23 = diccionario_palabras[22]
            palabras_para_imagen24 = diccionario_palabras[23]
            palabras_para_imagen25 = diccionario_palabras[24]
            palabras_para_imagen26 = diccionario_palabras[25]
            palabras_para_imagen27 = diccionario_palabras[26]
            palabras_para_imagen28 = diccionario_palabras[27]
            palabras_para_imagen29 = diccionario_palabras[28]
            palabras_para_imagen30 = diccionario_palabras[29]
            palabras_para_imagen31 = diccionario_palabras[30]
            palabras_para_imagen32 = diccionario_palabras[31]
            palabras_para_imagen33 = diccionario_palabras[32]
            palabras_para_imagen34 = diccionario_palabras[33]
            palabras_para_imagen35 = diccionario_palabras[34]
            palabras_para_imagen36 = diccionario_palabras[35]
            palabras_para_imagen37 = diccionario_palabras[36]

            random.shuffle(palabras_para_imagen1)
            random.shuffle(palabras_para_imagen2)
            random.shuffle(palabras_para_imagen3)
            random.shuffle(palabras_para_imagen4)
            random.shuffle(palabras_para_imagen5)
            random.shuffle(palabras_para_imagen6)
            random.shuffle(palabras_para_imagen7)
            random.shuffle(palabras_para_imagen8)
            random.shuffle(palabras_para_imagen9)
            random.shuffle(palabras_para_imagen10)
            random.shuffle(palabras_para_imagen11)
            random.shuffle(palabras_para_imagen12)
            random.shuffle(palabras_para_imagen13)
            random.shuffle(palabras_para_imagen14)
            random.shuffle(palabras_para_imagen15)
            random.shuffle(palabras_para_imagen16)
            random.shuffle(palabras_para_imagen17)
            random.shuffle(palabras_para_imagen18)
            random.shuffle(palabras_para_imagen19)
            random.shuffle(palabras_para_imagen20)
            random.shuffle(palabras_para_imagen21)
            random.shuffle(palabras_para_imagen22)
            random.shuffle(palabras_para_imagen23)
            random.shuffle(palabras_para_imagen24)
            random.shuffle(palabras_para_imagen25)
            random.shuffle(palabras_para_imagen26)
            random.shuffle(palabras_para_imagen27)
            random.shuffle(palabras_para_imagen28)
            random.shuffle(palabras_para_imagen29)
            random.shuffle(palabras_para_imagen30)
            random.shuffle(palabras_para_imagen31)
            random.shuffle(palabras_para_imagen32)
            random.shuffle(palabras_para_imagen33)
            random.shuffle(palabras_para_imagen34)
            random.shuffle(palabras_para_imagen35)
            random.shuffle(palabras_para_imagen36)
            random.shuffle(palabras_para_imagen37)

            p.vars['1'] = palabras_para_imagen1
            p.vars['2'] = palabras_para_imagen2
            p.vars['3'] = palabras_para_imagen3
            p.vars['4'] = palabras_para_imagen4
            p.vars['5'] = palabras_para_imagen5
            p.vars['6'] = palabras_para_imagen6
            p.vars['7'] = palabras_para_imagen7
            p.vars['8'] = palabras_para_imagen8
            p.vars['9'] = palabras_para_imagen9
            p.vars['10'] = palabras_para_imagen10
            p.vars['11'] = palabras_para_imagen11
            p.vars['12'] = palabras_para_imagen12
            p.vars['13'] = palabras_para_imagen13
            p.vars['14'] = palabras_para_imagen14
            p.vars['15'] = palabras_para_imagen15
            p.vars['16'] = palabras_para_imagen16
            p.vars['17'] = palabras_para_imagen17
            p.vars['18'] = palabras_para_imagen18
            p.vars['19'] = palabras_para_imagen19
            p.vars['20'] = palabras_para_imagen20
            p.vars['21'] = palabras_para_imagen21
            p.vars['22'] = palabras_para_imagen22
            p.vars['23'] = palabras_para_imagen23
            p.vars['24'] = palabras_para_imagen24
            p.vars['25'] = palabras_para_imagen25
            p.vars['26'] = palabras_para_imagen26
            p.vars['27'] = palabras_para_imagen27
            p.vars['28'] = palabras_para_imagen28
            p.vars['29'] = palabras_para_imagen29
            p.vars['30'] = palabras_para_imagen30
            p.vars['31'] = palabras_para_imagen31
            p.vars['32'] = palabras_para_imagen32
            p.vars['33'] = palabras_para_imagen33
            p.vars['34'] = palabras_para_imagen34
            p.vars['35'] = palabras_para_imagen35
            p.vars['36'] = palabras_para_imagen36
            p.vars['37'] = palabras_para_imagen37


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    palabraelegida = models.StringField(label= "¿Cuál palabra cree corresponde?")



    guardar_lista = models.StringField()


    imagen_palabra1 = models.StringField()

    imagen_palabra2 = models.StringField()

    imagen_palabra3 = models.StringField()

    imagen_palabra4 = models.StringField()

