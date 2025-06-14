import random

from confluent_kafka import Producer

from sensors import (
    LightSensor,
    MagneticSensor,
    GlassBreakSensor,
    MotionSensor,
    PressureSensor,
    VibrationSensor,
    SmartLockSensor,
    AnemometerSensor,
    BarometricPressureSensor,
    HumiditySensor,
    RainSensor,
    SolarRadiationSensor,
    TemperatureSensor,
    UVSensor,
    VisibilitySensor,
)


class SensorProvider:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__sensors = [
            LightSensor(),
            MagneticSensor(),
            GlassBreakSensor(),
            MotionSensor(),
            PressureSensor(),
            VibrationSensor(),
            SmartLockSensor(),
            AnemometerSensor(),
            BarometricPressureSensor(),
            HumiditySensor(),
            RainSensor(),
            SolarRadiationSensor(),
            TemperatureSensor(),
            UVSensor(),
            VisibilitySensor(),
            
        ]

    def sensor(self):
        return random.choice(self.__sensors)
    
    @property
    def sensors(self):
        return self.__sensors


if __name__ == "__main__":
    sensor_provider = SensorProvider()
    
    while True:
        for sensor in sensor_provider.sensors:
            data = sensor.read()
            print(data)

