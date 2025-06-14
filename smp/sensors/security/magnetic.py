from sensors.enums.location import Location
from sensors.enums.unit import Unit
from sensors.security.base import Base


class MagneticSensor(Base):
    def __init__(self):
        super().__init__()
        self._range = range(0, 1)
        self._unit = Unit.MAGNETIC

    def read(self):
        self._set_random_value()

        return self._serialize(self._to_dict())
