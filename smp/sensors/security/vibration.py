from sensors.enums.location import Location
from sensors.enums.unit import Unit
from sensors.security.base import Base


class VibrationSensor(Base):
    def __init__(self):
        super().__init__()
        self._unit = Unit.VIBRATION
        self._range = range(0, 100)  # Assuming vibration level is from 0 to 100
        
    def read(self):
        self._set_random_value()
        
        return self._serialize(self._to_dict())