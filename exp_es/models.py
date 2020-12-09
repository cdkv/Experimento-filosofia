from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'exp_es'
    players_per_group = None
    num_rounds = 1
    lista_videos = ['https://ucla.box.com/v/videostudymg', 'https://ucla.box.com/v/videostudysk',
                    'https://ucla.box.com/v/videostudynv', 'https://ucla.box.com/v/videostudyco',
                    'https://ucla.box.com/v/videostudyfb', 'https://ucla.box.com/v/videostudydo',
                    'https://ucla.box.com/v/videostudypg', 'https://ucla.box.com/v/videostudyda',
                    'https://ucla.box.com/v/videostudyin']

    palabras_imagen1 = ['celoso', 'en pánico', 'arrogante', 'lleno de odio',]

    palabras_imagen2 = ['juguetón', 'reconfortante', 'irritado', 'aburrido', ]

    palabras_imagen3 = ['aterrorizado', 'molesto', 'arrogante', 'enfadado', ]

    palabras_imagen4 = ['bromista', 'agobiada', 'deseo', 'convencida', ]

    palabras_imagen5 = ['bromista', 'insistente', 'entretenido', 'relajado', ]

    palabras_imagen6 = ['irritado', 'sarcástico', 'preocupado', 'amistoso', ]

    palabras_imagen7 = ['asustada', 'fantasiosa', 'impaciente', 'alarmada', ]

    palabras_imagen8 = ['arrepentido', 'amistoso', 'intranquilo', 'decaído', ]

    palabras_imagen9 = ['abatido', 'aliviado', 'tímido', 'entusiasmado', ]

    palabras_imagen10 = ['enfadada', 'hostil', 'horrorizada', 'angustiada', ]

    palabras_imagen11 = ['prudente', 'insistente', 'aburrido', 'asustado', ]

    palabras_imagen12 = ['aterrorizado', 'entretenido', 'arrepentido', 'seductor', ]

    palabras_imagen13 = ['indiferente', 'abochornado', 'escéptico', 'decaído', ]

    palabras_imagen14 = ['decidido', 'expectante', 'amenazante', 'tímido', ]

    palabras_imagen15 = ['irritado', 'decepcionado', 'deprimido', 'acusante', ]

    palabras_imagen16 = ['abstraída', 'agobiada', 'alentadora', 'entretenida', ]

    palabras_imagen17 = ['irritado', 'considerado', 'alentador', 'compasivo', ]

    palabras_imagen18 = ['insegura', 'afectuosa', 'juguetona', 'asustada', ]

    palabras_imagen19 = ['decidida', 'entretenida', 'asustada', 'aburrida', ]

    palabras_imagen20 = ['arrogante', 'agradecida', 'sarcástica', 'vacilante', ]

    palabras_imagen21 = ['imponente', 'amistoso', 'culpable', 'horrorizado', ]

    palabras_imagen22 = ['abochornada', 'fantasiosa', 'confundida', 'en pánico', ]

    palabras_imagen23 = ['angustiada', 'agradecida', 'insistente', 'suplicante', ]

    palabras_imagen24 = ['satisfecho', 'arrepentido', 'desafiante', 'curioso', ]

    palabras_imagen25 = ['abstraído', 'irritado', 'entusiasmado', 'hostil', ]

    palabras_imagen26 = ['en pánico', 'incrédula', 'abatida', 'interesada', ]

    palabras_imagen27 = ['alarmado', 'tímido', 'hostil', 'ansioso', ]

    palabras_imagen28 = ['bromista', 'prudente', 'arrogante', 'tranquilizadora', ]

    palabras_imagen29 = ['interesada', 'bromista', 'afectuosa', 'satisfecha', ]

    palabras_imagen30 = ['impaciente', 'asustada', 'irritada', 'reflexiva', ]

    palabras_imagen31 = ['agradecida', 'seductora', 'hostil', 'decepcionada', ]

    palabras_imagen32 = ['avergonzada', 'segura', 'bromista', 'decaída', ]

    palabras_imagen33 = ['serio', 'avergonzado', 'desconcertado', 'alarmado', ]

    palabras_imagen34 = ['abochornado', 'culpable', 'fantasioso', 'preocupado', ]

    palabras_imagen35 = ['asustada', 'desconcertada', 'recelosa', 'aterrorizada', ]

    palabras_imagen36 = ['perpleja', 'nerviosa', 'insistente', 'abstraída', ]

    palabras_imagen37 = ['avergonzado', 'nervioso', 'desconfiado', 'indeciso', ]

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            copialistavideos = Constants.lista_videos.copy()
            p.video1 = random.choice(copialistavideos)
            copialistavideos.remove(p.video1)
            p.video2 = random.choice(copialistavideos)
            copialistavideos.remove(p.video2)
            p.video3 = random.choice(copialistavideos)
            copialistavideos.remove(p.video3)
            p.video4 = random.choice(copialistavideos)
            copialistavideos.remove(p.video4)
            p.video5 = random.choice(copialistavideos)
            copialistavideos.remove(p.video5)
            p.video6 = random.choice(copialistavideos)
            copialistavideos.remove(p.video6)
            p.video7 = random.choice(copialistavideos)
            copialistavideos.remove(p.video7)
            p.video8 = random.choice(copialistavideos)
            copialistavideos.remove(p.video8)
            p.video9 = random.choice(copialistavideos)

            copiapalabrasimagen1 = Constants.palabras_imagen1.copy()
            copiapalabrasimagen2 = Constants.palabras_imagen2.copy()
            copiapalabrasimagen3 = Constants.palabras_imagen3.copy()
            copiapalabrasimagen4 = Constants.palabras_imagen4.copy()
            copiapalabrasimagen5 = Constants.palabras_imagen5.copy()
            copiapalabrasimagen6 = Constants.palabras_imagen6.copy()
            copiapalabrasimagen7 = Constants.palabras_imagen7.copy()
            copiapalabrasimagen8 = Constants.palabras_imagen8.copy()
            copiapalabrasimagen9 = Constants.palabras_imagen9.copy()
            copiapalabrasimagen10 = Constants.palabras_imagen10.copy()
            copiapalabrasimagen11 = Constants.palabras_imagen11.copy()
            copiapalabrasimagen12 = Constants.palabras_imagen12.copy()
            copiapalabrasimagen13 = Constants.palabras_imagen13.copy()
            copiapalabrasimagen14 = Constants.palabras_imagen14.copy()
            copiapalabrasimagen15 = Constants.palabras_imagen15.copy()
            copiapalabrasimagen16 = Constants.palabras_imagen16.copy()
            copiapalabrasimagen17 = Constants.palabras_imagen17.copy()
            copiapalabrasimagen18 = Constants.palabras_imagen18.copy()
            copiapalabrasimagen19 = Constants.palabras_imagen19.copy()
            copiapalabrasimagen20 = Constants.palabras_imagen20.copy()
            copiapalabrasimagen21 = Constants.palabras_imagen21.copy()
            copiapalabrasimagen22 = Constants.palabras_imagen22.copy()
            copiapalabrasimagen23 = Constants.palabras_imagen23.copy()
            copiapalabrasimagen24 = Constants.palabras_imagen24.copy()
            copiapalabrasimagen25 = Constants.palabras_imagen25.copy()
            copiapalabrasimagen26 = Constants.palabras_imagen26.copy()
            copiapalabrasimagen27 = Constants.palabras_imagen27.copy()
            copiapalabrasimagen28 = Constants.palabras_imagen28.copy()
            copiapalabrasimagen29 = Constants.palabras_imagen29.copy()
            copiapalabrasimagen30 = Constants.palabras_imagen30.copy()
            copiapalabrasimagen31 = Constants.palabras_imagen31.copy()
            copiapalabrasimagen32 = Constants.palabras_imagen32.copy()
            copiapalabrasimagen33 = Constants.palabras_imagen33.copy()
            copiapalabrasimagen34 = Constants.palabras_imagen34.copy()
            copiapalabrasimagen35 = Constants.palabras_imagen35.copy()
            copiapalabrasimagen36 = Constants.palabras_imagen36.copy()
            copiapalabrasimagen37 = Constants.palabras_imagen37.copy()
            p.imagen1_palabra1 =random.choice(copiapalabrasimagen1)
            copiapalabrasimagen1.remove(p.imagen1_palabra1)
            p.imagen1_palabra2 =random.choice(copiapalabrasimagen1)
            copiapalabrasimagen1.remove(p.imagen1_palabra2)
            p.imagen1_palabra3 =random.choice(copiapalabrasimagen1)
            copiapalabrasimagen1.remove(p.imagen1_palabra3)
            p.imagen1_palabra4 =random.choice(copiapalabrasimagen1)


            p.imagen2_palabra1 =random.choice(copiapalabrasimagen2)
            copiapalabrasimagen2.remove(p.imagen2_palabra1)
            p.imagen2_palabra2 =random.choice(copiapalabrasimagen2)
            copiapalabrasimagen2.remove(p.imagen2_palabra2)
            p.imagen2_palabra3 =random.choice(copiapalabrasimagen2)
            copiapalabrasimagen2.remove(p.imagen2_palabra3)
            p.imagen2_palabra4 =random.choice(copiapalabrasimagen2)


            p.imagen3_palabra1 =random.choice(copiapalabrasimagen3)
            copiapalabrasimagen3.remove(p.imagen3_palabra1)
            p.imagen3_palabra2 =random.choice(copiapalabrasimagen3)
            copiapalabrasimagen3.remove(p.imagen3_palabra2)
            p.imagen3_palabra3 =random.choice(copiapalabrasimagen3)
            copiapalabrasimagen3.remove(p.imagen3_palabra3)
            p.imagen3_palabra4 =random.choice(copiapalabrasimagen3)


            p.imagen4_palabra1 =random.choice(copiapalabrasimagen4)
            copiapalabrasimagen4.remove(p.imagen4_palabra1)
            p.imagen4_palabra2 =random.choice(copiapalabrasimagen4)
            copiapalabrasimagen4.remove(p.imagen4_palabra2)
            p.imagen4_palabra3 =random.choice(copiapalabrasimagen4)
            copiapalabrasimagen4.remove(p.imagen4_palabra3)
            p.imagen4_palabra4 =random.choice(copiapalabrasimagen4)


            p.imagen5_palabra1 =random.choice(copiapalabrasimagen5)
            copiapalabrasimagen5.remove(p.imagen5_palabra1)
            p.imagen5_palabra2 =random.choice(copiapalabrasimagen5)
            copiapalabrasimagen5.remove(p.imagen5_palabra2)
            p.imagen5_palabra3 =random.choice(copiapalabrasimagen5)
            copiapalabrasimagen5.remove(p.imagen5_palabra3)
            p.imagen5_palabra4 =random.choice(copiapalabrasimagen5)


            p.imagen6_palabra1 =random.choice(copiapalabrasimagen6)
            copiapalabrasimagen6.remove(p.imagen6_palabra1)
            p.imagen6_palabra2 =random.choice(copiapalabrasimagen6)
            copiapalabrasimagen6.remove(p.imagen6_palabra2)
            p.imagen6_palabra3 =random.choice(copiapalabrasimagen6)
            copiapalabrasimagen6.remove(p.imagen6_palabra3)
            p.imagen6_palabra4 =random.choice(copiapalabrasimagen6)


            p.imagen7_palabra1 =random.choice(copiapalabrasimagen7)
            copiapalabrasimagen7.remove(p.imagen7_palabra1)
            p.imagen7_palabra2 =random.choice(copiapalabrasimagen7)
            copiapalabrasimagen7.remove(p.imagen7_palabra2)
            p.imagen7_palabra3 =random.choice(copiapalabrasimagen7)
            copiapalabrasimagen7.remove(p.imagen7_palabra3)
            p.imagen7_palabra4 =random.choice(copiapalabrasimagen7)



            p.imagen8_palabra1 =random.choice(copiapalabrasimagen8)
            copiapalabrasimagen8.remove(p.imagen8_palabra1)
            p.imagen8_palabra2 =random.choice(copiapalabrasimagen8)
            copiapalabrasimagen8.remove(p.imagen8_palabra2)
            p.imagen8_palabra3 =random.choice(copiapalabrasimagen8)
            copiapalabrasimagen8.remove(p.imagen8_palabra3)
            p.imagen8_palabra4 =random.choice(copiapalabrasimagen8)


            p.imagen9_palabra1 =random.choice(copiapalabrasimagen9)
            copiapalabrasimagen9.remove(p.imagen9_palabra1)
            p.imagen9_palabra2 =random.choice(copiapalabrasimagen9)
            copiapalabrasimagen9.remove(p.imagen9_palabra2)
            p.imagen9_palabra3 =random.choice(copiapalabrasimagen9)
            copiapalabrasimagen9.remove(p.imagen9_palabra3)
            p.imagen9_palabra4 =random.choice(copiapalabrasimagen9)


            p.imagen10_palabra1 =random.choice(copiapalabrasimagen10)
            copiapalabrasimagen10.remove(p.imagen10_palabra1)
            p.imagen10_palabra2 =random.choice(copiapalabrasimagen10)
            copiapalabrasimagen10.remove(p.imagen10_palabra2)
            p.imagen10_palabra3 =random.choice(copiapalabrasimagen10)
            copiapalabrasimagen10.remove(p.imagen10_palabra3)
            p.imagen10_palabra4 =random.choice(copiapalabrasimagen10)


            p.imagen11_palabra1 =random.choice(copiapalabrasimagen11)
            copiapalabrasimagen11.remove(p.imagen11_palabra1)
            p.imagen11_palabra2 =random.choice(copiapalabrasimagen11)
            copiapalabrasimagen11.remove(p.imagen11_palabra2)
            p.imagen11_palabra3 =random.choice(copiapalabrasimagen11)
            copiapalabrasimagen11.remove(p.imagen11_palabra3)
            p.imagen11_palabra4 =random.choice(copiapalabrasimagen11)


            p.imagen12_palabra1 =random.choice(copiapalabrasimagen12)
            copiapalabrasimagen12.remove(p.imagen12_palabra1)
            p.imagen12_palabra2 =random.choice(copiapalabrasimagen12)
            copiapalabrasimagen12.remove(p.imagen12_palabra2)
            p.imagen12_palabra3 =random.choice(copiapalabrasimagen12)
            copiapalabrasimagen12.remove(p.imagen12_palabra3)
            p.imagen12_palabra4 =random.choice(copiapalabrasimagen12)


            p.imagen13_palabra1 =random.choice(copiapalabrasimagen13)
            copiapalabrasimagen13.remove(p.imagen13_palabra1)
            p.imagen13_palabra2 =random.choice(copiapalabrasimagen13)
            copiapalabrasimagen13.remove(p.imagen13_palabra2)
            p.imagen13_palabra3 =random.choice(copiapalabrasimagen13)
            copiapalabrasimagen13.remove(p.imagen13_palabra3)
            p.imagen13_palabra4 =random.choice(copiapalabrasimagen13)


            p.imagen14_palabra1 =random.choice(copiapalabrasimagen14)
            copiapalabrasimagen14.remove(p.imagen14_palabra1)
            p.imagen14_palabra2 =random.choice(copiapalabrasimagen14)
            copiapalabrasimagen14.remove(p.imagen14_palabra2)
            p.imagen14_palabra3 =random.choice(copiapalabrasimagen14)
            copiapalabrasimagen14.remove(p.imagen14_palabra3)
            p.imagen14_palabra4 =random.choice(copiapalabrasimagen14)


            p.imagen15_palabra1 =random.choice(copiapalabrasimagen15)
            copiapalabrasimagen15.remove(p.imagen15_palabra1)
            p.imagen15_palabra2 =random.choice(copiapalabrasimagen15)
            copiapalabrasimagen15.remove(p.imagen15_palabra2)
            p.imagen15_palabra3 =random.choice(copiapalabrasimagen15)
            copiapalabrasimagen15.remove(p.imagen15_palabra3)
            p.imagen15_palabra4 =random.choice(copiapalabrasimagen15)


            p.imagen16_palabra1 =random.choice(copiapalabrasimagen16)
            copiapalabrasimagen16.remove(p.imagen16_palabra1)
            p.imagen16_palabra2 =random.choice(copiapalabrasimagen16)
            copiapalabrasimagen16.remove(p.imagen16_palabra2)
            p.imagen16_palabra3 =random.choice(copiapalabrasimagen16)
            copiapalabrasimagen16.remove(p.imagen16_palabra3)
            p.imagen16_palabra4 =random.choice(copiapalabrasimagen16)


            p.imagen17_palabra1 =random.choice(copiapalabrasimagen17)
            copiapalabrasimagen17.remove(p.imagen17_palabra1)
            p.imagen17_palabra2 =random.choice(copiapalabrasimagen17)
            copiapalabrasimagen17.remove(p.imagen17_palabra2)
            p.imagen17_palabra3 =random.choice(copiapalabrasimagen17)
            copiapalabrasimagen17.remove(p.imagen17_palabra3)
            p.imagen17_palabra4 =random.choice(copiapalabrasimagen17)


            p.imagen18_palabra1 =random.choice(copiapalabrasimagen18)
            copiapalabrasimagen18.remove(p.imagen18_palabra1)
            p.imagen18_palabra2 =random.choice(copiapalabrasimagen18)
            copiapalabrasimagen18.remove(p.imagen18_palabra2)
            p.imagen18_palabra3 =random.choice(copiapalabrasimagen18)
            copiapalabrasimagen18.remove(p.imagen18_palabra3)
            p.imagen18_palabra4 =random.choice(copiapalabrasimagen18)


            p.imagen19_palabra1 =random.choice(copiapalabrasimagen19)
            copiapalabrasimagen19.remove(p.imagen19_palabra1)
            p.imagen19_palabra2 =random.choice(copiapalabrasimagen19)
            copiapalabrasimagen19.remove(p.imagen19_palabra2)
            p.imagen19_palabra3 =random.choice(copiapalabrasimagen19)
            copiapalabrasimagen19.remove(p.imagen19_palabra3)
            p.imagen19_palabra4 =random.choice(copiapalabrasimagen19)


            p.imagen20_palabra1 =random.choice(copiapalabrasimagen20)
            copiapalabrasimagen20.remove(p.imagen20_palabra1)
            p.imagen20_palabra2 =random.choice(copiapalabrasimagen20)
            copiapalabrasimagen20.remove(p.imagen20_palabra2)
            p.imagen20_palabra3 =random.choice(copiapalabrasimagen20)
            copiapalabrasimagen20.remove(p.imagen20_palabra3)
            p.imagen20_palabra4 =random.choice(copiapalabrasimagen20)


            p.imagen21_palabra1 =random.choice(copiapalabrasimagen21)
            copiapalabrasimagen21.remove(p.imagen21_palabra1)
            p.imagen21_palabra2 =random.choice(copiapalabrasimagen21)
            copiapalabrasimagen21.remove(p.imagen21_palabra2)
            p.imagen21_palabra3 =random.choice(copiapalabrasimagen21)
            copiapalabrasimagen21.remove(p.imagen21_palabra3)
            p.imagen21_palabra4 =random.choice(copiapalabrasimagen21)


            p.imagen22_palabra1 =random.choice(copiapalabrasimagen22)
            copiapalabrasimagen22.remove(p.imagen22_palabra1)
            p.imagen22_palabra2 =random.choice(copiapalabrasimagen22)
            copiapalabrasimagen22.remove(p.imagen22_palabra2)
            p.imagen22_palabra3 =random.choice(copiapalabrasimagen22)
            copiapalabrasimagen22.remove(p.imagen22_palabra3)
            p.imagen22_palabra4 =random.choice(copiapalabrasimagen22)


            p.imagen23_palabra1 =random.choice(copiapalabrasimagen23)
            copiapalabrasimagen23.remove(p.imagen23_palabra1)
            p.imagen23_palabra2 =random.choice(copiapalabrasimagen23)
            copiapalabrasimagen23.remove(p.imagen23_palabra2)
            p.imagen23_palabra3 =random.choice(copiapalabrasimagen23)
            copiapalabrasimagen23.remove(p.imagen23_palabra3)
            p.imagen23_palabra4 =random.choice(copiapalabrasimagen23)


            p.imagen24_palabra1 =random.choice(copiapalabrasimagen24)
            copiapalabrasimagen24.remove(p.imagen24_palabra1)
            p.imagen24_palabra2 =random.choice(copiapalabrasimagen24)
            copiapalabrasimagen24.remove(p.imagen24_palabra2)
            p.imagen24_palabra3 =random.choice(copiapalabrasimagen24)
            copiapalabrasimagen24.remove(p.imagen24_palabra3)
            p.imagen24_palabra4 =random.choice(copiapalabrasimagen24)


            p.imagen25_palabra1 =random.choice(copiapalabrasimagen25)
            copiapalabrasimagen25.remove(p.imagen25_palabra1)
            p.imagen25_palabra2 =random.choice(copiapalabrasimagen25)
            copiapalabrasimagen25.remove(p.imagen25_palabra2)
            p.imagen25_palabra3 =random.choice(copiapalabrasimagen25)
            copiapalabrasimagen25.remove(p.imagen25_palabra3)
            p.imagen25_palabra4 =random.choice(copiapalabrasimagen25)


            p.imagen26_palabra1 =random.choice(copiapalabrasimagen26)
            copiapalabrasimagen26.remove(p.imagen26_palabra1)
            p.imagen26_palabra2 =random.choice(copiapalabrasimagen26)
            copiapalabrasimagen26.remove(p.imagen26_palabra2)
            p.imagen26_palabra3 =random.choice(copiapalabrasimagen26)
            copiapalabrasimagen26.remove(p.imagen26_palabra3)
            p.imagen26_palabra4 =random.choice(copiapalabrasimagen26)


            p.imagen27_palabra1 =random.choice(copiapalabrasimagen27)
            copiapalabrasimagen27.remove(p.imagen27_palabra1)
            p.imagen27_palabra2 =random.choice(copiapalabrasimagen27)
            copiapalabrasimagen27.remove(p.imagen27_palabra2)
            p.imagen27_palabra3 =random.choice(copiapalabrasimagen27)
            copiapalabrasimagen27.remove(p.imagen27_palabra3)
            p.imagen27_palabra4 =random.choice(copiapalabrasimagen27)


            p.imagen28_palabra1 =random.choice(copiapalabrasimagen28)
            copiapalabrasimagen28.remove(p.imagen28_palabra1)
            p.imagen28_palabra2 =random.choice(copiapalabrasimagen28)
            copiapalabrasimagen28.remove(p.imagen28_palabra2)
            p.imagen28_palabra3 =random.choice(copiapalabrasimagen28)
            copiapalabrasimagen28.remove(p.imagen28_palabra3)
            p.imagen28_palabra4 =random.choice(copiapalabrasimagen28)


            p.imagen29_palabra1 =random.choice(copiapalabrasimagen29)
            copiapalabrasimagen29.remove(p.imagen29_palabra1)
            p.imagen29_palabra2 =random.choice(copiapalabrasimagen29)
            copiapalabrasimagen29.remove(p.imagen29_palabra2)
            p.imagen29_palabra3 =random.choice(copiapalabrasimagen29)
            copiapalabrasimagen29.remove(p.imagen29_palabra3)
            p.imagen29_palabra4 =random.choice(copiapalabrasimagen29)


            p.imagen30_palabra1 =random.choice(copiapalabrasimagen30)
            copiapalabrasimagen30.remove(p.imagen30_palabra1)
            p.imagen30_palabra2 =random.choice(copiapalabrasimagen30)
            copiapalabrasimagen30.remove(p.imagen30_palabra2)
            p.imagen30_palabra3 =random.choice(copiapalabrasimagen30)
            copiapalabrasimagen30.remove(p.imagen30_palabra3)
            p.imagen30_palabra4 =random.choice(copiapalabrasimagen30)


            p.imagen31_palabra1 =random.choice(copiapalabrasimagen31)
            copiapalabrasimagen31.remove(p.imagen31_palabra1)
            p.imagen31_palabra2 =random.choice(copiapalabrasimagen31)
            copiapalabrasimagen31.remove(p.imagen31_palabra2)
            p.imagen31_palabra3 =random.choice(copiapalabrasimagen31)
            copiapalabrasimagen31.remove(p.imagen31_palabra3)
            p.imagen31_palabra4 =random.choice(copiapalabrasimagen31)


            p.imagen32_palabra1 =random.choice(copiapalabrasimagen32)
            copiapalabrasimagen32.remove(p.imagen32_palabra1)
            p.imagen32_palabra2 =random.choice(copiapalabrasimagen32)
            copiapalabrasimagen32.remove(p.imagen32_palabra2)
            p.imagen32_palabra3 =random.choice(copiapalabrasimagen32)
            copiapalabrasimagen32.remove(p.imagen32_palabra3)
            p.imagen32_palabra4 =random.choice(copiapalabrasimagen32)


            p.imagen33_palabra1 =random.choice(copiapalabrasimagen33)
            copiapalabrasimagen33.remove(p.imagen33_palabra1)
            p.imagen33_palabra2 =random.choice(copiapalabrasimagen33)
            copiapalabrasimagen33.remove(p.imagen33_palabra2)
            p.imagen33_palabra3 =random.choice(copiapalabrasimagen33)
            copiapalabrasimagen33.remove(p.imagen33_palabra3)
            p.imagen33_palabra4 =random.choice(copiapalabrasimagen33)


            p.imagen34_palabra1 =random.choice(copiapalabrasimagen34)
            copiapalabrasimagen34.remove(p.imagen34_palabra1)
            p.imagen34_palabra2 =random.choice(copiapalabrasimagen34)
            copiapalabrasimagen34.remove(p.imagen34_palabra2)
            p.imagen34_palabra3 =random.choice(copiapalabrasimagen34)
            copiapalabrasimagen34.remove(p.imagen34_palabra3)
            p.imagen34_palabra4 =random.choice(copiapalabrasimagen34)


            p.imagen35_palabra1 =random.choice(copiapalabrasimagen35)
            copiapalabrasimagen35.remove(p.imagen35_palabra1)
            p.imagen35_palabra2 =random.choice(copiapalabrasimagen35)
            copiapalabrasimagen35.remove(p.imagen35_palabra2)
            p.imagen35_palabra3 =random.choice(copiapalabrasimagen35)
            copiapalabrasimagen35.remove(p.imagen35_palabra3)
            p.imagen35_palabra4 =random.choice(copiapalabrasimagen35)


            p.imagen36_palabra1 =random.choice(copiapalabrasimagen36)
            copiapalabrasimagen36.remove(p.imagen36_palabra1)
            p.imagen36_palabra2 =random.choice(copiapalabrasimagen36)
            copiapalabrasimagen36.remove(p.imagen36_palabra2)
            p.imagen36_palabra3 =random.choice(copiapalabrasimagen36)
            copiapalabrasimagen36.remove(p.imagen36_palabra3)
            p.imagen36_palabra4 =random.choice(copiapalabrasimagen36)


            p.imagen37_palabra1 =random.choice(copiapalabrasimagen37)
            copiapalabrasimagen37.remove(p.imagen37_palabra1)
            p.imagen37_palabra2 =random.choice(copiapalabrasimagen37)
            copiapalabrasimagen37.remove(p.imagen37_palabra2)
            p.imagen37_palabra3 =random.choice(copiapalabrasimagen37)
            copiapalabrasimagen37.remove(p.imagen37_palabra3)
            p.imagen37_palabra4 =random.choice(copiapalabrasimagen37)



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    consentimiento = models.StringField(
        choices=['Si', 'No'],
        widget=widgets.RadioSelect)

    dificultad_video = models.StringField(
        choices=['Si', 'No'],
        widget=widgets.RadioSelect)

    vi_1_des= models.LongStringField(blank=True)

    dia_nacimiento = models.IntegerField(
        label='¿En qué mes naciste?',
        min=1, max=31)

    mes_nacimiento = models.IntegerField(
        label='¿En qué mes naciste?',
        min=1, max=12)

    fecha_nacimiento = models.IntegerField(
        label='¿En qué año naciste?',
        min=1900, max=2020)


    genero = models.StringField(
        choices=['Hombre', 'Mujer', 'Otro', 'no proviene respuesta'],
        label='¿Con qué género se identifica?',
        widget=widgets.RadioSelect)

    otro_genero = models.StringField(label='Si desea, especifique su género', blank=True)

    idiomas1 = models.StringField(
        choices=['africaans', 'árabe', 'chapalaa', 'chino', 'croata', 'checo', 'inglés', 'francés', 'hindi', 'isizulu',
                 'japonés', 'coreano', 'polaco', 'quechua', 'ruso', 'serbio', 'setswana', 'shuar', 'eslovaco', 'español', 'ucranio', 'huaorani', 'otro', 'no proviene respuesta'],
        label='',
        )

    idiomas2 = models.StringField(
        choices=['africaans', 'árabe', 'chapalaa', 'chino', 'croata', 'checo', 'inglés', 'francés', 'hindi', 'isizulu',
                 'japonés', 'coreano', 'polaco', 'quechua', 'ruso', 'serbio', 'setswana', 'shuar', 'eslovaco', 'español', 'ucranio', 'huaorani', 'otro', 'no proviene respuesta'],
        label='',
        )

    idiomas3 = models.StringField(
        choices=['africaans', 'árabe', 'chapalaa', 'chino', 'croata', 'checo', 'inglés', 'francés', 'hindi', 'isizulu',
                 'japonés', 'coreano', 'polaco', 'quechua', 'ruso', 'serbio', 'setswana', 'shuar', 'eslovaco', 'español', 'ucranio', 'huaorani', 'otro', 'no proviene respuesta'],
        label='',
        )

    si_otro_idioma1 = models.StringField(
        choices=['Si', 'No'],
        widget=widgets.RadioSelect)

    si_otro_idioma2 = models.StringField(
        choices=['Si', 'No'],
        widget=widgets.RadioSelect)


    video1 = models.StringField()

    video2 = models.StringField()

    video3 = models.StringField()

    video4 = models.StringField()

    video5 = models.StringField()

    video6 = models.StringField()

    video7 = models.StringField()

    video8 = models.StringField()

    video9 = models.StringField()



    palabraelegida1 = models.StringField(label= "¿Cuál palabra cree corresponde?")

    palabraelegida2 = models.StringField()

    palabraelegida3 = models.StringField()

    palabraelegida4 = models.StringField()

    palabraelegida5 = models.StringField()

    palabraelegida6 = models.StringField()

    palabraelegida7 = models.StringField()

    palabraelegida8 = models.StringField()

    palabraelegida9 = models.StringField()

    palabraelegida10 = models.StringField()

    palabraelegida11 = models.StringField()

    palabraelegida12 = models.StringField()

    palabraelegida13 = models.StringField()

    palabraelegida14 = models.StringField()

    palabraelegida15 = models.StringField()

    palabraelegida16 = models.StringField()

    palabraelegida17 = models.StringField()

    palabraelegida18 = models.StringField()

    palabraelegida19 = models.StringField()

    palabraelegida20 = models.StringField()

    palabraelegida21 = models.StringField()

    palabraelegida22 = models.StringField()

    palabraelegida23 = models.StringField()

    palabraelegida24 = models.StringField()

    palabraelegida25 = models.StringField()

    palabraelegida26 = models.StringField()

    palabraelegida27 = models.StringField()

    palabraelegida28 = models.StringField()

    palabraelegida29 = models.StringField()

    palabraelegida30 = models.StringField()

    palabraelegida31 = models.StringField()

    palabraelegida32 = models.StringField()

    palabraelegida33 = models.StringField()

    palabraelegida34 = models.StringField()

    palabraelegida35 = models.StringField()

    palabraelegida36 = models.StringField()

    palabraelegida37 = models.StringField()



    def palabraelegida1_choices(self):
        copiapalabrasimagen1=Constants.palabras_imagen1.copy()
        choices = copiapalabrasimagen1
        random.shuffle(choices)
        return choices


    def palabraelegida2_choices(self):
        copiapalabrasimagen2=Constants.palabras_imagen2.copy()
        choices = copiapalabrasimagen2
        random.shuffle(choices)
        return choices


    def palabraelegida3_choices(self):
        copiapalabrasimagen3=Constants.palabras_imagen3.copy()
        choices = copiapalabrasimagen3
        random.shuffle(choices)
        return choices

    def palabraelegida4_choices(self):
        copiapalabrasimagen4=Constants.palabras_imagen4.copy()
        choices = copiapalabrasimagen4
        random.shuffle(choices)
        return choices

    def palabraelegida5_choices(self):
        import random
        copiapalabrasimagen5=Constants.palabras_imagen5.copy()
        choices = copiapalabrasimagen5
        random.shuffle(choices)
        return choices

    def palabraelegida6_choices(self):
        copiapalabrasimagen6=Constants.palabras_imagen6.copy()
        choices = copiapalabrasimagen6
        random.shuffle(choices)
        return choices

    def palabraelegida7_choices(self):
        copiapalabrasimagen7=Constants.palabras_imagen7.copy()
        choices = copiapalabrasimagen7
        random.shuffle(choices)
        return choices

    def palabraelegida8_choices(self):
        copiapalabrasimagen8=Constants.palabras_imagen8.copy()
        choices = copiapalabrasimagen8
        random.shuffle(choices)
        return choices

    def palabraelegida9_choices(self):
        copiapalabrasimagen9=Constants.palabras_imagen9.copy()
        choices = copiapalabrasimagen9
        random.shuffle(choices)
        return choices

    def palabraelegida10_choices(self):
        copiapalabrasimagen10=Constants.palabras_imagen10.copy()
        choices = copiapalabrasimagen10
        random.shuffle(choices)
        return choices

    def palabraelegida11_choices(self):
        copiapalabrasimagen11=Constants.palabras_imagen11.copy()
        choices = copiapalabrasimagen11
        random.shuffle(choices)
        return choices

    def palabraelegida12_choices(self):
        copiapalabrasimagen12=Constants.palabras_imagen12.copy()
        choices = copiapalabrasimagen12
        random.shuffle(choices)
        return choices

    def palabraelegida13_choices(self):
        copiapalabrasimagen13=Constants.palabras_imagen13.copy()
        choices = copiapalabrasimagen13
        random.shuffle(choices)
        return choices

    def palabraelegida14_choices(self):
        copiapalabrasimagen14=Constants.palabras_imagen14.copy()
        choices = copiapalabrasimagen14
        random.shuffle(choices)
        return choices

    def palabraelegida15_choices(self):
        copiapalabrasimagen15=Constants.palabras_imagen15.copy()
        choices = copiapalabrasimagen15
        random.shuffle(choices)
        return choices

    def palabraelegida16_choices(self):
        copiapalabrasimagen16=Constants.palabras_imagen16.copy()
        choices = copiapalabrasimagen16
        random.shuffle(choices)
        return choices

    def palabraelegida17_choices(self):
        copiapalabrasimagen17=Constants.palabras_imagen17.copy()
        choices = copiapalabrasimagen17
        random.shuffle(choices)
        return choices

    def palabraelegida18_choices(self):
        copiapalabrasimagen18=Constants.palabras_imagen18.copy()
        choices = copiapalabrasimagen18
        random.shuffle(choices)
        return choices

    def palabraelegida19_choices(self):
        copiapalabrasimagen19=Constants.palabras_imagen19.copy()
        choices = copiapalabrasimagen19
        random.shuffle(choices)
        return choices

    def palabraelegida20_choices(self):
        copiapalabrasimagen20=Constants.palabras_imagen20.copy()
        choices = copiapalabrasimagen20
        random.shuffle(choices)
        return choices

    def palabraelegida21_choices(self):
        copiapalabrasimagen21=Constants.palabras_imagen21.copy()
        choices = copiapalabrasimagen21
        random.shuffle(choices)
        return choices

    def palabraelegida22_choices(self):
        copiapalabrasimagen22=Constants.palabras_imagen22.copy()
        choices = copiapalabrasimagen22
        random.shuffle(choices)
        return choices

    def palabraelegida23_choices(self):
        copiapalabrasimagen23=Constants.palabras_imagen23.copy()
        choices = copiapalabrasimagen23
        random.shuffle(choices)
        return choices

    def palabraelegida24_choices(self):
        copiapalabrasimagen24=Constants.palabras_imagen24.copy()
        choices = copiapalabrasimagen24
        random.shuffle(choices)
        return choices

    def palabraelegida25_choices(self):
        copiapalabrasimagen25=Constants.palabras_imagen25.copy()
        choices = copiapalabrasimagen25
        random.shuffle(choices)
        return choices

    def palabraelegida26_choices(self):
        copiapalabrasimagen26=Constants.palabras_imagen26.copy()
        choices = copiapalabrasimagen26
        random.shuffle(choices)
        return choices

    def palabraelegida27_choices(self):
        copiapalabrasimagen27=Constants.palabras_imagen27.copy()
        choices = copiapalabrasimagen27
        random.shuffle(choices)
        return choices

    def palabraelegida28_choices(self):
        copiapalabrasimagen28=Constants.palabras_imagen28.copy()
        choices = copiapalabrasimagen28
        random.shuffle(choices)
        return choices

    def palabraelegida29_choices(self):
        copiapalabrasimagen29=Constants.palabras_imagen29.copy()
        choices = copiapalabrasimagen29
        random.shuffle(choices)
        return choices

    def palabraelegida30_choices(self):
        copiapalabrasimagen30=Constants.palabras_imagen30.copy()
        choices = copiapalabrasimagen30
        random.shuffle(choices)
        return choices

    def palabraelegida31_choices(self):
        copiapalabrasimagen31=Constants.palabras_imagen31.copy()
        choices = copiapalabrasimagen31
        random.shuffle(choices)
        return choices

    def palabraelegida32_choices(self):
        copiapalabrasimagen32=Constants.palabras_imagen32.copy()
        choices = copiapalabrasimagen32
        random.shuffle(choices)
        return choices

    def palabraelegida33_choices(self):
        copiapalabrasimagen33=Constants.palabras_imagen33.copy()
        choices = copiapalabrasimagen33
        random.shuffle(choices)
        return choices

    def palabraelegida34_choices(self):
        copiapalabrasimagen34=Constants.palabras_imagen34.copy()
        choices = copiapalabrasimagen34
        random.shuffle(choices)
        return choices

    def palabraelegida35_choices(self):
        copiapalabrasimagen35=Constants.palabras_imagen35.copy()
        choices = copiapalabrasimagen35
        random.shuffle(choices)
        return choices

    def palabraelegida36_choices(self):
        copiapalabrasimagen36=Constants.palabras_imagen36.copy()
        choices = copiapalabrasimagen36
        random.shuffle(choices)
        return choices

    def palabraelegida37_choices(self):
        copiapalabrasimagen37=Constants.palabras_imagen37.copy()
        choices = copiapalabrasimagen37
        random.shuffle(choices)
        return choices

    imagen1_palabra1 = models.StringField()

    imagen1_palabra2 = models.StringField()

    imagen1_palabra3 = models.StringField()

    imagen1_palabra4 = models.StringField()


    imagen2_palabra1 = models.StringField()

    imagen2_palabra2 = models.StringField()

    imagen2_palabra3 = models.StringField()

    imagen2_palabra4 = models.StringField()


    imagen3_palabra1 = models.StringField()

    imagen3_palabra2 = models.StringField()

    imagen3_palabra3 = models.StringField()

    imagen3_palabra4 = models.StringField()


    imagen4_palabra1 = models.StringField()

    imagen4_palabra2 = models.StringField()

    imagen4_palabra3 = models.StringField()

    imagen4_palabra4 = models.StringField()


    imagen5_palabra1 = models.StringField()

    imagen5_palabra2 = models.StringField()

    imagen5_palabra3 = models.StringField()

    imagen5_palabra4 = models.StringField()


    imagen6_palabra1 = models.StringField()

    imagen6_palabra2 = models.StringField()

    imagen6_palabra3 = models.StringField()

    imagen6_palabra4 = models.StringField()


    imagen7_palabra1 = models.StringField()

    imagen7_palabra2 = models.StringField()

    imagen7_palabra3 = models.StringField()

    imagen7_palabra4 = models.StringField()


    imagen8_palabra1 = models.StringField()

    imagen8_palabra2 = models.StringField()

    imagen8_palabra3 = models.StringField()

    imagen8_palabra4 = models.StringField()


    imagen9_palabra1 = models.StringField()

    imagen9_palabra2 = models.StringField()

    imagen9_palabra3 = models.StringField()

    imagen9_palabra4 = models.StringField()


    imagen10_palabra1 = models.StringField()

    imagen10_palabra2 = models.StringField()

    imagen10_palabra3 = models.StringField()

    imagen10_palabra4 = models.StringField()


    imagen11_palabra1 = models.StringField()

    imagen11_palabra2 = models.StringField()

    imagen11_palabra3 = models.StringField()

    imagen11_palabra4 = models.StringField()


    imagen12_palabra1 = models.StringField()

    imagen12_palabra2 = models.StringField()

    imagen12_palabra3 = models.StringField()

    imagen12_palabra4 = models.StringField()


    imagen13_palabra1 = models.StringField()

    imagen13_palabra2 = models.StringField()

    imagen13_palabra3 = models.StringField()

    imagen13_palabra4 = models.StringField()


    imagen14_palabra1 = models.StringField()

    imagen14_palabra2 = models.StringField()

    imagen14_palabra3 = models.StringField()

    imagen14_palabra4 = models.StringField()


    imagen15_palabra1 = models.StringField()

    imagen15_palabra2 = models.StringField()

    imagen15_palabra3 = models.StringField()

    imagen15_palabra4 = models.StringField()


    imagen16_palabra1 = models.StringField()

    imagen16_palabra2 = models.StringField()

    imagen16_palabra3 = models.StringField()

    imagen16_palabra4 = models.StringField()


    imagen17_palabra1 = models.StringField()

    imagen17_palabra2 = models.StringField()

    imagen17_palabra3 = models.StringField()

    imagen17_palabra4 = models.StringField()


    imagen18_palabra1 = models.StringField()

    imagen18_palabra2 = models.StringField()

    imagen18_palabra3 = models.StringField()

    imagen18_palabra4 = models.StringField()


    imagen19_palabra1 = models.StringField()

    imagen19_palabra2 = models.StringField()

    imagen19_palabra3 = models.StringField()

    imagen19_palabra4 = models.StringField()


    imagen20_palabra1 = models.StringField()

    imagen20_palabra2 = models.StringField()

    imagen20_palabra3 = models.StringField()

    imagen20_palabra4 = models.StringField()


    imagen21_palabra1 = models.StringField()

    imagen21_palabra2 = models.StringField()

    imagen21_palabra3 = models.StringField()

    imagen21_palabra4 = models.StringField()


    imagen22_palabra1 = models.StringField()

    imagen22_palabra2 = models.StringField()

    imagen22_palabra3 = models.StringField()

    imagen22_palabra4 = models.StringField()


    imagen23_palabra1 = models.StringField()

    imagen23_palabra2 = models.StringField()

    imagen23_palabra3 = models.StringField()

    imagen23_palabra4 = models.StringField()


    imagen24_palabra1 = models.StringField()

    imagen24_palabra2 = models.StringField()

    imagen24_palabra3 = models.StringField()

    imagen24_palabra4 = models.StringField()


    imagen25_palabra1 = models.StringField()

    imagen25_palabra2 = models.StringField()

    imagen25_palabra3 = models.StringField()

    imagen25_palabra4 = models.StringField()


    imagen26_palabra1 = models.StringField()

    imagen26_palabra2 = models.StringField()

    imagen26_palabra3 = models.StringField()

    imagen26_palabra4 = models.StringField()


    imagen27_palabra1 = models.StringField()

    imagen27_palabra2 = models.StringField()

    imagen27_palabra3 = models.StringField()

    imagen27_palabra4 = models.StringField()


    imagen28_palabra1 = models.StringField()

    imagen28_palabra2 = models.StringField()

    imagen28_palabra3 = models.StringField()

    imagen28_palabra4 = models.StringField()


    imagen29_palabra1 = models.StringField()

    imagen29_palabra2 = models.StringField()

    imagen29_palabra3 = models.StringField()

    imagen29_palabra4 = models.StringField()


    imagen30_palabra1 = models.StringField()

    imagen30_palabra2 = models.StringField()

    imagen30_palabra3 = models.StringField()

    imagen30_palabra4 = models.StringField()


    imagen31_palabra1 = models.StringField()

    imagen31_palabra2 = models.StringField()

    imagen31_palabra3 = models.StringField()

    imagen31_palabra4 = models.StringField()


    imagen32_palabra1 = models.StringField()

    imagen32_palabra2 = models.StringField()

    imagen32_palabra3 = models.StringField()

    imagen32_palabra4 = models.StringField()


    imagen33_palabra1 = models.StringField()

    imagen33_palabra2 = models.StringField()

    imagen33_palabra3 = models.StringField()

    imagen33_palabra4 = models.StringField()


    imagen34_palabra1 = models.StringField()

    imagen34_palabra2 = models.StringField()

    imagen34_palabra3 = models.StringField()

    imagen34_palabra4 = models.StringField()


    imagen35_palabra1 = models.StringField()

    imagen35_palabra2 = models.StringField()

    imagen35_palabra3 = models.StringField()

    imagen35_palabra4 = models.StringField()


    imagen36_palabra1 = models.StringField()

    imagen36_palabra2 = models.StringField()

    imagen36_palabra3 = models.StringField()

    imagen36_palabra4 = models.StringField()


    imagen37_palabra1 = models.StringField()

    imagen37_palabra2 = models.StringField()

    imagen37_palabra3 = models.StringField()

    imagen37_palabra4 = models.StringField()

