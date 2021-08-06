
class PrimaryCharacteristicCandidate:
    def __init__(self, dx, dy, u_radius, sens_field_radius, etalon):
        self.dx = dx
        self.dy = dy
        self.u_radius = u_radius
        self.sens_field_radius = sens_field_radius
        self.etalon = etalon
        self.conditional_activations = []


class UnitCharacteristicCandidate:
    def __init__(self, unit, dx, dy):
        self.dx = dx
        self.dy = dy
        self.unit = unit
        self.conditional_activations = []


class PrimaryCharacteristic:
    def __init__(self, candidate, quality):
        self.dx = candidate.dx
        self.dy= candidate.dy
        self.u_radius = candidate.u_radius
        self.sens_field_radius = candidate.sens_field_radius
        self.etalon = candidate.etalon
        self.quality = quality
        self.conditional_probs = None
        self.bins = None

    def get_likelihood(self,activation):
        # вероятсность того, что отклонение от эталона это или меньше - сложить куч бинов
        pass

class UnitCharacteristic:
    def __init__(self, candidate, quality):
        self.dx = candidate.dx
        self.dy = candidate.dy
        self.unit = candidate.unit
        self.quality = quality
        self.conditional_probs = None

    def get_likelihood(self, activation):
        if activation == 0:
            return self.conditional_probs[0]
        return self.conditional_probs[1]

class Characteristics:
    def __init__(self):
        self.not_sorted = []

    def to_dict(self):
        pass



