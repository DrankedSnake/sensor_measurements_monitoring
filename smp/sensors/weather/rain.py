import random
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class RainSensor(Base):
    def __init__(self):
        super().__init__()
        self._range = range(0, 1)
        

    def read(self) -> str:
        self._unit = Unit.RAIN
        self._set_random_value()

        return self._serialize(self._to_dict())