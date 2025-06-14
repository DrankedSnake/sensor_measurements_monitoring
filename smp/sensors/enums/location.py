from __future__ import annotations

from enum import Enum
from typing import List


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

    def weather_sensors() -> List[Location]:
        return [
            Location.OUTDOOR,
            Location.INDOOR,
            Location.ROOFTOP,
            Location.GARDEN,
            Location.BALCONY,
            Location.POOL_AREA,
        ]

    def security_sensors() -> List[Location]:
        return [
            Location.FRONT_DOOR,
            Location.BACK_DOOR,
            Location.GARAGE,
            Location.LIVING_ROOM,
            Location.BEDROOM,
            Location.KITCHEN,
            Location.BASEMENT,
            Location.ATTIC,
            Location.PERIMETER,
        ]
