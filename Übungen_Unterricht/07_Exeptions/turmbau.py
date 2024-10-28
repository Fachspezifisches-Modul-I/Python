import random


class TurmEinsturzFehler(Exception):
    def __init__(self, message):
        super().__init__(message)


def baue_den_turm_auf():

    if (random.random() < 0.2):
        raise TurmEinsturzFehler('Der Turm ist zusammengefallen')
    print('Yay, der Turm steht')


for _ in range(10):
        baue_den_turm_auf()
