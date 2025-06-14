from sensors.abstract import AbstractSensor
from sensors.enums.sensor_state import State
from sensors.enums.sensor_type import Type
from sensors.enums.unit import Unit


class Base(AbstractSensor):
    """
    Base class for security sensors.
    """

    def __init__(self):
        self._type = Type.WEATHER
        self._state = State.ON
        self._value = None
        self._unit: Unit = None
