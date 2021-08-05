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


    def grow_current_sprouts(self, pic, x, y, current_sprouts=None):
        if isinstance(self.match_finder, PrimaryUnit):
            pass
        else:
            pass

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









"""
отсев ростков по достижении верхнего  (по максимуму правдоподобия характеристик)"""

