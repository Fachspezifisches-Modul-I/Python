# Wir bauen einen Turm
from random import random


class TurmIstEingefallenFehler(Exception):

    def __init__(self, message=''):
        super().__init__(message)


class Kind():

    def baue_turm_auf(self):
        if random() < 0.2:
            raise TurmIstEingefallenFehler()
        return 'Der Turm lebt! gut gemacht :)'


k = Kind()
print(k.baue_turm_auf())

# TODO Zu erledigen
# FIXME Die bude brennt!
