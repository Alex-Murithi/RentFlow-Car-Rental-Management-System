# rental_system.py

from rental import Rental
from vehicle import SUV, LuxuryCar, EconomyCar

class CarRentalSystem:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.customers = []
        self.rentals = []
        self.payments = []
        self.__revenue = 0   # Encapsulation

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def register_customer(self, customer):
        self.customers.append(customer)

    def find_vehicle(self, reg_number):
        return next((v for v in self.vehicles if v.registration_number == reg_number), None)

    def find_customer(self, customer_id):
        return next((c for c in self.customers if c.customer_id == customer_id), None)

    def show_available_vehicles(self):
        print("Available Vehicles:")
        for v in self.vehicles:
            if v.is_available():
                v.display_details()

    def rent_vehicle(self, customer, vehicle, days):
        if customer not in self.customers:
            raise ValueError("Customer not registered.")
        if vehicle not in self.vehicles:
            raise ValueError("Vehicle not in fleet.")
        if not vehicle.is_available():
            raise ValueError("Vehicle not available.")
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        rental_id = f"R{len(self.rentals)+1:03d}"
        rental = Rental(rental_id, customer, vehicle, days)
        vehicle.mark_as_rented()
        customer.add_rental(rental)
        self.rentals.append(rental)
        return rental

    def return_vehicle(self, rental, actual_days, damage_charge=0):
        if rental.status != "ACTIVE":
            raise ValueError("Rental not active.")
        rental.complete_rental(actual_days, damage_charge)
        rental.vehicle.mark_as_available()

    def process_payment(self, payment):
        success = payment.process_payment()
        if success:
            self.__revenue += payment.amount
            self.payments.append(payment)

    @property
    def revenue(self):
        return self.__revenue

    def generate_report(self):
        print("=====================================")
        print(f"    {self.name.upper()} MANAGEMENT REPORT")
        print("=====================================")
        print(f"Total Vehicles:              {len(self.vehicles)}")
        print(f"Available Vehicles:          {sum(v.is_available() for v in self.vehicles)}")
        print(f"Rented Vehicles:             {sum(not v.is_available() for v in self.vehicles)}")
        print(f"Registered Customers:        {len(self.customers)}")
        print(f"Total Rentals:               {len(self.rentals)}")
        print(f"Active Rentals:              {sum(r.status == 'ACTIVE' for r in self.rentals)}")
        print(f"Completed Rentals:           {sum(r.status == 'COMPLETED' for r in self.rentals)}")
        print()
        print(f"Total Revenue:      KSh {self.__revenue}")
        print("-------------------------------------")
        print("VEHICLES BY CATEGORY")
        print(f"Economy Cars:                {sum(isinstance(v, EconomyCar) for v in self.vehicles)}")
        print(f"SUVs:                        {sum(isinstance(v, SUV) for v in self.vehicles)}")
        print(f"Luxury Cars:                 {sum(isinstance(v, LuxuryCar) for v in self.vehicles)}")
        print("=====================================")
