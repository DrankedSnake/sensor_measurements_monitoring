from smp.sensors.abstract import AbstractSensor
from smp.sensors.enums.sensor_state import State
from smp.sensors.enums.sensor_type import Type


class Base(AbstractSensor):
    """
    Base class for security sensors.
    """

    def __init__(self):
        self._type = Type.SECURITY
        self._state = State.ON
        self._value = None