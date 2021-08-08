from units_stat_carrier import *

def get_start_unit_for_this_unit(unit):
    start_unit = unit
    while True:
        if start_unit.prev_unit is None:
            return start_unit
        start_unit = start_unit.prev_unit

def gather_stat_for_unit(unit, pics):
    start_unit = get_start_unit_for_this_unit(unit)