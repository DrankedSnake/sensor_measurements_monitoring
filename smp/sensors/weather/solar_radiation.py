import random
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class SolarRadiationSensor(Base):
    def __init__(self):
        super().__init__()
        self._range = range(0, 1000)

    def read(self) -> str:
        self._unit = random.choice([Unit.SOLAR_WATTS_PER_M2, Unit.SOLAR_BTUS_PER_FT2])
        self._set_random_value()
        
        return self._serialize(self._to_dict())