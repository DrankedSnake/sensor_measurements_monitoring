from confluent_kafka import Producer
import random
import json

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
    def __init__(self):
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


def delivery_report(err, msg):
    """
    Callback for Kafka delivery reports.
    """
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")


if __name__ == "__main__":
    kafka_config = {
        "bootstrap.servers": "kafka:9092",
    }
    producer = Producer(kafka_config)

    sensor_provider = SensorProvider()

    try:
        while True:
            for sensor in sensor_provider.sensors:
                data = sensor.read()
                # print(f"Generated data: {data}")

                serialized_data = json.dumps(data)
                # print(f"Serialized data: {serialized_data}")

                producer.produce(
                    topic="sensor-data",
                    key=str(sensor.__class__.__name__),
                    value=serialized_data,
                    callback=delivery_report,
                )
                producer.poll(0)

    except KeyboardInterrupt:
        print("Stopping sensor data producer...")
    finally:
        producer.flush()
