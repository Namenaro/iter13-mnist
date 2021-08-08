from unit import *
from primary_unit import *

class Recognizer:
    def __init__(self, start_unit, goal_unit_id=None):
        self.start_unit = start_unit
        self.goal_unit_id = goal_unit_id

    def try_start_sprouts(self, x, y, pic):
        matches_coords_ranged = self.start_unit.match_finder.find_matches(pic, x, y)

        if len(matches_coords_ranged) == 0:
            return []  # ни один росток не растет с самого начала

        sprouts = []
        for i in range(len(matches_coords_ranged)):
            # добавляем ростков "единичной" высоты
            x = matches_coords_ranged[i][0]
            y = matches_coords_ranged[i][1]
            match = Match(self.start_unit, x, y)
            sprout = [match]  # росток это список матчей
            sprouts.append(sprout)
        return sprouts

    def grow_top_sprout(self, current_sprouts, pic):
        if len(current_sprouts) == 0:
            return
        # выбираем ранее сработавший юнит, из которого сейчас будем "доращивать"
        best_sprout = current_sprouts[0]
        top_note = best_sprout[-1]

        # делаем проростки из места срабатывания предыдущего юнита в ростке
        mini_sprouts = self.apply_unit(self, top_note.unit.next_unit, top_note.x, top_note.y, pic)

        if len(mini_sprouts) == 0:
            # лучший росток пришел в тупик, удяляем из рассмотрения
            current_sprouts.pop(0)  # TODO если он дорос до А, регать событие А?
        else:
            # удаляем лучший росток, и заменяем его на н штук новых сортированных лучших ростков
            # "на единицу" выше старого лучшего
            new_best_sprouts = []
            for mini_sprout in mini_sprouts:
                new_sprout = list(current_sprouts[0]) + mini_sprout
                new_best_sprouts.append(new_sprout)

            current_sprouts.pop(0)
            current_sprouts = new_best_sprouts + current_sprouts

    def apply_unit(self, unit, x, y, pic):
        if isinstance(unit.match_finder, PrimaryUnit):
            XYs = unit.match_finder.find_matches(pic, x, y)
            sprouts = []
            for xy in XYs:
                sprout = [Match(unit, x=xy[0], y=xy[1])]
                sprouts.append(sprout)
            return sprouts

        return Recognizer(start_unit=unit).recognize(x, y, pic)

    def is_top_sprout_ended(self, current_sprouts):
        best_sprout = current_sprouts[0]
        top_of_best_sprout = best_sprout[-1]
        last_unit = top_of_best_sprout.unit
        if self.goal_unit_id is None:
            if last_unit.next_unit is None:
                return True
            return False
        else:
            if last_unit.id == self.goal_unit_id:
                return True
            return False


    def move_ended_sprouts_to_results(self, current_sprouts, full_sprouts):
        while True:
            if len(current_sprouts) == 0:
                break
            if self.is_top_sprout_ended(current_sprouts):
                full_sprouts.append(current_sprouts[0])
                current_sprouts.pop(0)
            else:
                break

    def recognize(self, x, y, pic):
        result_sprouts = []
        current_sprouts = self.try_start_sprouts(x, y, pic)

        while True:
            if len(current_sprouts) == 0:
                return result_sprouts
            self.move_ended_sprouts_to_results(current_sprouts, result_sprouts)
            self.grow_top_sprout(self, current_sprouts, pic)
