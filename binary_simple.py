from sensors import *
from stat_database import *

class Match:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class BinaryExperiment:
    def __init__(self, u_radius, sensor_field_radius, sensory_min, sensory_max):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.sensory_min = sensory_min
        self.sensory_max = sensory_max


    def run(self, pic, anchorx, anchory):
        matches_ranged = []
        for r in range(0, self.u_radius + 1):
            X, Y = get_coords_for_radius(anchorx, anchory, r)
            for i in range(len(X)):
                activation = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
                if activation >= self.sensory_min and activation <= self.sensory_max:
                    match = Match(dx=X[i]-anchorx, dy = Y[i]-anchory)
                    matches_ranged.append(match)
        return matches_ranged

    def unconditional_probability_of_match(self):
        return get_probability_of_eventA(minA=self.sensory_min,
                                         maxA=self.sensory_max,
                                         sensor_field_radius= self.sensor_field_radius,
                                         u_radius=self.u_radius)




