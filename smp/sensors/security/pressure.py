import random
from sensors.enums.location import Location
from sensors.enums.unit import Unit
from sensors.security.base import Base


class PressureSensor(Base):
    def __init__(self):
        super().__init__()

    def read(self) -> str:
        self._unit = random.choice((Unit.BAROMETRIC_PRESSURE_HP, Unit.BAROMETRIC_PRESSURE_MB))  # Unit for pressure
        self._range = range(950, 1050) if self._unit == Unit.BAROMETRIC_PRESSURE_MB else range(28, 31)
        self._value = self._random_value(self._range)  # Generate a random pressure value within the range
        self._datetime = self._datetime_now()
        self._location = self._random_location(Location.security_sensors())
        
        return self._serialize(self._to_dict())  # Serialize the sensor data