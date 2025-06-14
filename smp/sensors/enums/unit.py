from enum import Enum


class Unit(Enum):
    # Weather Sensor Units
    TEMPERATURE_C = "°C"
    TEMPERATURE_F = "°F"
    HUMIDITY = "%"
    BAROMETRIC_PRESSURE_HP = "hPa"
    BAROMETRIC_PRESSURE_MB = "mbar"
    RAIN = ""
    ANEMOMETER_MS = "m/s"
    ANEMOMETER_KMS = "km/h"
    WIND_VANE = "°"
    SOLAR_WATTS_PER_M2 = "W/m²"
    SOLAR_BTUS_PER_FT2 = "BTU/ft²"
    UV_SENSOR = "UV Index"
    SOIL_MOISTURE = "%"
    VISIBILITY_M = "m"
    VISIBILITY_KM = "km"

    # Security Sensor Units
    GLASS_BREAK = "breaks"
    MOTION = ""
    LOCK = ""
    SMOKE_DETECTOR = "ppm"  # Parts per million
    CO_DETECTOR = "ppm"  # Parts per million
    WATER_LEAK = ""
    GAS_LEAK = "ppm"  # Parts per million
    LIGHT = "lux"
    MAGNETIC = ""
    VIBRATION = ""  # Custom unit for vibration sensors