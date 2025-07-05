import random
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class TemperatureSensor(Base):
    def __init__(self):
        super().__init__()

    def read(self) -> str:
        self._unit = random.choice([Unit.TEMPERATURE_C, Unit.TEMPERATURE_F])
        self._range = range(-30, 50) if self._unit == Unit.TEMPERATURE_C else range(-22, 122)
        self._value = random.randint(self._range.start, self._range.stop - 1)
        self._set_random_value()

        return self._serialize(self._to_dict())
