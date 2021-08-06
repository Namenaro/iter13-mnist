from primary_unit import *

import uuid

class Unit: #управление на данный нейрон может быть передано только другим нейроном
    def __init__(self, dx,dy, match_finder, prev_unit=None):
        self.id = str(uuid.uuid4())

        self.dx = dx
        self.dy = dy

        self.match_finder = match_finder

        self.characteristisc = None
        self.label_hist = None
        self.next_units = []
        self.prev_unit = prev_unit
        self.unconditional_probability_of_match = self._count_unconditional_probability_of_match()


    def _count_unconditional_probability_of_match(self):
        # безусловная вероятность, что текущий эксперимент в отрыве от предыстории получит успех
        if isinstance(self.match_finder, PrimaryUnit):
            current_experiment_success_probability = self.match_finder.unconditional_probability_of_match_in_xy()
        else:
            current_experiment_success_probability = self.match_finder.unconditional_probability_of_match

        # если предыстории нет, то вернем вероятность успеха этого эксперимента:
        if self.prev_neuron is None:
            return current_experiment_success_probability

        # если предыстория есть, то надо помножить вероятность текущего успеха на вероятность успеха предыстории:
        return self.prev_neuron.unconditional_probability_of_match * current_experiment_success_probability


class Match:
    def __init__(self, unit, x,y):
        self.unit = unit
        self.x = x
        self.y = y

class Grower:
    def __init__(self, start_unit, pic):
        self.start_unit = start_unit
        self.pic = pic


    def try_start_history(self, x, y):
        matches_coords_ranged = self.start_unit.match_finder.find_matches(self.pic, x, y)

        if len(matches_coords_ranged) == 0:
            return None # ни один росток не растет с самого начала

        sprouts = []
        for i in range(len(matches_coords_ranged)):
            # добавляем ростков "единичной" высоты
            x = matches_coords_ranged[i][0]
            y = matches_coords_ranged[i][1]
            match = Match(self.start_unit, x, y)
            sprout = [match]   # росток это список матчей
            sprouts.append(sprout)
        return sprouts

    def try_continue_history(self, sprouts):
        if len(sprouts) == 0: # все имеющиеся на рассмотрении ростки пришли в тупик
            return None
