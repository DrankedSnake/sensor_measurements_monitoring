import random
from sensors.enums.location import Location
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class BarometricPressureSensor(Base):
    def __init__(self):
        super().__init__()

    def read(self):
        self._unit = random.choice([Unit.BAROMETRIC_PRESSURE_HP, Unit.BAROMETRIC_PRESSURE_MB])
        self._range = range(950, 1050) if self._unit == Unit.BAROMETRIC_PRESSURE_HP else range(28, 31)
        self._set_random_value()

        return self._serialize(self._to_dict())
