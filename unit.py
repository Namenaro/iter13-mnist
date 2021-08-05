from primary_unit import *

import uuid

class Unit: #управление на данный нейрон может быть передано только другим нейроном
    def __init__(self, dx,dy, match_finder, prev_neuron=None):
        self.id = str(uuid.uuid4())

        self.dx = dx
        self.dy = dy

        self.match_finder = match_finder
        self.characteristisc = None
        self.next_neuron = None
        self.prev_neuron = prev_neuron
        self.unconditional_probability_of_match=self._count_unconditional_probability_of_match()


    def find_matches(self, pic, anchorx, anchory):
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

        # если предыстории есть, то надо помножить вероятность текущего успеха на вероятность успеха предыстории:
        return self.prev_neuron.unconditional_probability_of_match * current_experiment_success_probability









"""гистограмма меток
предыдущий мотив
следующий мотив
характеристики
левел
вероятность срабатывания с попправкой на ю

отсев ростков по достижении верхнего  (по максимуму правдоподобия характеристик)"""

class UnitBlacklist:
    def __init__(self):
        self.Xs = []
        self.Ys = []
        self.sensor_field_radiuses = []

    def check_if_in(self,x,y,sensor_field_radius):
        if x in self.Xs:
            if y in self.Ys:
                if sensor_field_radius in self.sensor_field_radiuses:
                    return True
        return False
