import random
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class TemperatureSensor(Base):
    def __init__(self):
        super().__init__()
        
    def read(self) -> str:
        self._set_random_value()
        self._unit = random.choice([Unit.TEMPERATURE_CELSIUS, Unit.TEMPERATURE_FAHRENHEIT])
        self._range = range(-30, 50) if self._unit == Unit.TEMPERATURE_CELSIUS else range(-22, 122)
        self._value = random.randint(self._range.start, self._range.stop - 1)
                
        return self._serialize(self._to_dict())
