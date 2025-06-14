from sensors.enums.unit import Unit
from sensors.weather.base import Base


class UVSensor(Base):
    def __init__(self):
        super().__init__()
        self._unit = Unit.UV_SENSOR
        self._range = range(0, 11)
    
    def read(self):
        self._set_random_value()
        
        return self._serialize(self._to_dict())
