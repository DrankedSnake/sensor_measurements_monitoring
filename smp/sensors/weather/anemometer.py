import random
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class AnemometerSensor(Base):
    def __init__(self):
        super().__init__()
        self._range = range(0, 100)
    
    def read(self):
        self._unit = random.choice([Unit.ANEMOMETER_MS, Unit.ANEMOMETER_KMS])
        self._set_random_value()
        
        return self._serialize(self._to_dict())
