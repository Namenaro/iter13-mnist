

class UnitSproutBlacklist:
    def __init__(self):
        self.Xs = []
        self.Ys = []
        self.sensor_field_radiuses = []

    def check_if_in(self,x, y, sensor_field_radius):
        if x in self.Xs:
            if y in self.Ys:
                if sensor_field_radius in self.sensor_field_radiuses:
                    return True
        return False
