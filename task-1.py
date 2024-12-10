from abc import ABC, abstractmethod
import logging
from typing import Type

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass

class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")

if __name__ == "__main__":
    us_factory: VehicleFactory = USVehicleFactory()
    us_car: Vehicle = us_factory.create_car("Ford", "Mustang")
    us_motorcycle: Vehicle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    us_car.start_engine()
    us_motorcycle.start_engine()

    eu_factory: VehicleFactory = EUVehicleFactory()
    eu_car: Vehicle = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle: Vehicle = eu_factory.create_motorcycle("Ducati", "Panigale")

    eu_car.start_engine()
    eu_motorcycle.start_engine()
