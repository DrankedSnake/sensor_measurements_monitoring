from sensors.abstract import AbstractSensor
from sensors.enums.location import Location
from sensors.enums.sensor_state import State
from sensors.enums.sensor_type import Type


class Base(AbstractSensor):
    """
    Base class for security sensors.
    """

    def __init__(self):
        super().__init__()
        self._type = Type.SECURITY
