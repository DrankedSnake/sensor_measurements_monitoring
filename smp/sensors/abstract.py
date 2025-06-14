import json
import random
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Callable, List

from sensors.enums.location import Location
from sensors.enums.sensor_state import State
from sensors.enums.sensor_type import Type
from sensors.enums.unit import Unit


class AbstractSensor(ABC):
    """
    Abstract base class for sensors.
    """

    def __init__(self):
        self._type: Type = None
        self._state: State = None
        self._value: float = None
        self._range: range = None
        self._unit: Unit = None
        self._location: Location = None
        self._datetime: datetime = None

    def _to_dict(self) -> dict:
        return {
            self._check_attributes(key, value): value
            for key, value in self.__dict__.items()
        }

    def _check_attributes(self, key, value) -> str:
        if isinstance(value, Callable):
            return False
        else:
            if key.startswith("_"):
                return key[1:]
            return key

    def _serialize(self, data: dict) -> str:
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            if isinstance(value, Enum):
                data[key] = value.value
            if isinstance(value, range):
                data[key] = (value.start, value.stop)

        return json.dumps(data)

    def _datetime_now(self) -> datetime:
        """
        Get the current datetime.
        """
        return datetime.now()

    def _random_location(self, locations: List[Location]) -> Location:
        """
        Get a random location from the Location enum.
        """
        return random.choice(locations)

    def _random_value(self, value_range: range) -> float:
        """
        Get a random value within the specified range.
        """
        return float(random.randint(value_range.start, value_range.stop))

    @abstractmethod
    def read(self):
        """
        Read data from the sensor.
        """
        pass
        """
        Calibrate the sensor.
        """
        pass
