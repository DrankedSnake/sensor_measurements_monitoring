from sensors.enums.location import Location
from sensors.enums.unit import Unit
from sensors.security.base import Base


class LightSensor(Base):
    def __init__(self):
        super().__init__()
        self._range = range(0, 2000)
        self._unit = Unit.LIGHT

    def read(self):
        """
        Simulate reading the light sensor value.
        """
        self._set_random_value()
        
        return self._serialize(self._to_dict())
