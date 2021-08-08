from recognizer import *

"""Целенаправленный сбор активаций для конкретного юнита"""

class UnitStatCarrier:
    def __init__(self, characterisics):
        self.characterisics = characterisics

        # копим просто все активации в виде списков:
        self.labels_data = []
        self.characterisics_data = {}
        for key in characterisics.keys():
            self.characterisics_data[key]=[]


    def register_new_situation(self, pic, label, sprout):
        self.labels.append(label)
        for caracteristic_id in self.characteristics.keys():
            val = self.characteristics[caracteristic_id].apply(sprout,pic)
            self.characterisics_data[caracteristic_id].append(val)


def get_start_unit_for_this_unit(unit):
    start_unit = unit
    while True:
        if start_unit.prev_unit is None:
            return start_unit
        start_unit = start_unit.prev_unit

def gather_stat_for_unit(unit, pics, labels, characterisics):
    start_unit = get_start_unit_for_this_unit(unit)
    unit_stat = UnitStatCarrier(unit, characterisics)
    recognizer = Recognizer(start_unit, unit.id)

    ymax = pics[0].shape[0]
    xmax = pics[0].shape[1]
    for i in range(len(pics)):
        pic = pics[i]
        label = labels[i]

        for y in range(0, ymax):
            for x in range(0, xmax):
                sprouts = recognizer.recognize(x,y,pic)
                for sprout in sprouts:
                    unit_stat.register_new_situation(pic, label,sprout)
    return unit_stat