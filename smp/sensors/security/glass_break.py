from sensors.enums.location import Location
from sensors.enums.unit import Unit
from sensors.security.base import Base


class GlassBreakSensor(Base):
    def __init__(self):
        super().__init__()
        self._range = range(0, 1)
        self._unit = Unit.GLASS_BREAK

    def read(self) -> str:
        self._value = self._random_value(self._range)
        self._location = self._random_location(Location.security_sensors())
        self._datetime = self._datetime_now()

        return self._serialize(self._to_dict())
