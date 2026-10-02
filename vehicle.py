# vehicle.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, registration_number, make, model, year, daily_rate):
        if daily_rate < 0:
            raise ValueError("Daily rate cannot be negative.")
        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.__available = True   # Encapsulation

    def display_details(self):
        status = "Available" if self.__available else "Rented"
        print(f"{self.year} {self.make} {self.model} ({self.registration_number}) - {status}")

    def is_available(self):
        return self.__available

    def mark_as_rented(self):
        self.__available = False

    def mark_as_available(self):
        self.__available = True

    @abstractmethod
    def calculate_rental_cost(self, days):
        """Each subclass must implement its own pricing rule."""
        pass


class EconomyCar(Vehicle):
    def calculate_rental_cost(self, days):
        # Economy cars: daily_rate × days
        return self.daily_rate * days


class SUV(Vehicle):
    def calculate_rental_cost(self, days):
        # SUVs: daily_rate × days + one-time service charge
        return (self.daily_rate * days) + 2000


class LuxuryCar(Vehicle):
    def calculate_rental_cost(self, days):
        # Luxury cars: daily_rate × days + 10% insurance
        base = self.daily_rate * days
        insurance = base * 0.10
        return base + insurance
