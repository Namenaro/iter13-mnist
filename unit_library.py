# запоминаем все стратовые юниты (те, у которых нет предыдущего)
# нужны методы создать и сохранить, работающие в 2 фазы: сначала заполняем все,
# кроме перекрестных ссылок, а потом заполняем ссылки на юниты.

class Memory:
    def __init__(self):
        self.start_units = []

    def to_json(self, json_name):
        pass

    def from_json(self, json_name):
        pass

    def apply_to_pic(self,pic):
        pass
