import random
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class VisibilitySensor(Base):
    def __init__(self):
        super().__init__()

    def read(self):
        self._unit = random.choice([Unit.VISIBILITY_M, Unit.VISIBILITY_KM])
        self._range = range(0, 10000) if self._unit == Unit.VISIBILITY_M else range(0, 10)
        self._set_random_value()

        return self._serialize(self._to_dict())
