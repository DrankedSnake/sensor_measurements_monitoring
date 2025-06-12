from abc import ( 
    ABC,
    abstractmethod,
)


class AbstractSensor(ABC):
    """
    Abstract base class for sensors.
    """

    @abstractmethod
    def read(self):
        """
        Read data from the sensor.
        """
        pass

    @abstractmethod
    def calibrate(self):
        """
        Calibrate the sensor.
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Reset the sensor to its initial state.
        """
        pass
