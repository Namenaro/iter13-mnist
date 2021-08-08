class UnitStatCarrier:
    def __init__(self, unit, characterisics):
        self.unit = unit
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