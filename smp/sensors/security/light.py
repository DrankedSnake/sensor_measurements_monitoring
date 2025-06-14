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
        self._value = self._random_value(self._range)
        self._datetime = self._datetime_now()
        self._location = self._random_location(Location.security_sensors())
        
        return self._serialize(self._to_dict())
