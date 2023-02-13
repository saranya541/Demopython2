
from django.db import models

# Create your models here.

MALAPPURAM = 'malappuram'
ERANAKKULAM='eranakkulam'
KOZHIKODE ='kozhikode'
WAYANAD='wayanad'
THISSUR = 'thrissur'




M_1 = 'Vengara'
M_2 = 'Kottakkal'
M_3 = 'Perithalmanna'
M_4 = 'Edappal'
M_5 = 'Manjeri'
E_1 = 'Aluva'
E_2 = 'Kochi'
E_3 = 'Edapallly'
E_4 = 'Paravur'
E_5 = 'Angamaly'
K_1 = 'Mavoor'
K_2 = 'Mukkam'
K_3 = 'Koyilandi'
K_4 = 'Ramanattukara'
K_5 = 'Feroke'
W_1 = 'Mananthavady'
W_2 = 'kalpetta'
W_3 = 'Panamaram'
T_1 = 'Chavakkad'
T_2 = 'Chalakkudy'
T_3 = 'Irinjalakuda'






DISTRICT_CHOICES = [
    (MALAPPURAM,MALAPPURAM),
    (ERANAKKULAM,ERANAKKULAM),
    (KOZHIKODE,KOZHIKODE),
    (WAYANAD,WAYANAD),
    (THISSUR,THISSUR),
]

BRANCH_CHOICES= [
    (M_1, M_1),
    (M_2, M_2),
    (M_3, M_3),
    (M_4, M_4),
    (M_5, M_5),
    (E_1, E_1),
    (E_2, E_2),
    (E_3, E_3),
    (E_4, E_4),
    (E_5, E_5),
    (K_1, K_1),
    (K_2, K_2),
    (K_3, K_3),
    (K_4, K_4),
    (K_5, K_5),
    (W_1, W_1),
    (W_2, W_2),
    (W_3, W_3),
    (T_1, T_1),
    (T_2, T_2),
    (T_3, T_3),
]

def get_m_strings():
    m_strings = [
        M_1,
        M_2,
        M_3,
        M_4,
        M_5,
    ]

    return m_strings


def get_e_strings():
    e_strings = [
        E_1,
        E_2,
        E_3,
        E_4,
        E_5,
    ]

    return e_strings

def get_k_strings():
    k_strings = [
        K_1,
        K_2,
        K_3,
        K_4,
        K_5,
    ]

    return k_strings
def get_w_strings():
    w_strings = [
        W_1,
        W_2,
        W_3,
    ]

    return w_strings
def get_t_strings():
    t_strings = [
        T_1,
        T_2,
        T_3,
    ]

    return t_strings



class Person(models.Model):
    # id_name
    # name = models.CharField(max_length=50)
    # id_department
    district= models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    # id_courses
    branch= models.CharField(max_length=50, choices=BRANCH_CHOICES)

