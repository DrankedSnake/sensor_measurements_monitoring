from sensors.enums.location import Location
from sensors.enums.unit import Unit
from sensors.weather.base import Base


class HumiditySensor(Base):
    def __init__(self):
        super().__init__()
        self._unit = Unit.HUMIDITY
        self._range = range(0, 100)

    def read(self):
        self._set_random_value()

        return self._serialize(self._to_dict())
