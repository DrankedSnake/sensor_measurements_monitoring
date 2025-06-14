from __future__ import annotations

from enum import Enum
from typing import List

from sensors.enums.sensor_type import Type


class Location(Enum):
    # Weather Sensor Locations
    OUTDOOR = "Outdoor"
    INDOOR = "Indoor"
    ROOFTOP = "Rooftop"
    GARDEN = "Garden"
    BALCONY = "Balcony"
    POOL_AREA = "Pool Area"

    # Security Sensor Locations
    FRONT_DOOR = "Front Door"
    BACK_DOOR = "Back Door"
    GARAGE = "Garage"
    LIVING_ROOM = "Living Room"
    BEDROOM = "Bedroom"
    KITCHEN = "Kitchen"
    BASEMENT = "Basement"
    ATTIC = "Attic"
    PERIMETER = "Perimeter"

    @classmethod
    def __weather_sensors(cls) -> List[Location]:
        return [
            cls.OUTDOOR,
            cls.INDOOR,
            cls.ROOFTOP,
            cls.GARDEN,
            cls.BALCONY,
            cls.POOL_AREA,
        ]

    @classmethod
    def __security_sensors(cls) -> List[Location]:
        return [
            cls.FRONT_DOOR,
            cls.BACK_DOOR,
            cls.GARAGE,
            cls.LIVING_ROOM,
            cls.BEDROOM,
            cls.KITCHEN,
            cls.BASEMENT,
            cls.ATTIC,
            cls.PERIMETER,
        ]
        
    @classmethod
    def sensors(cls, sensor_type: Type) -> List[Location]:
        return cls.__weather_sensors() if sensor_type == Type.WEATHER else cls.__security_sensors()
