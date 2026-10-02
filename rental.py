# rental.py

from vehicle import SUV, LuxuryCar  # ✅ import the subclasses you need

class Rental:
    def __init__(self, rental_id, customer, vehicle, rental_days):
        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.actual_days = None
        self.status = "ACTIVE"
        self.base_cost = vehicle.calculate_rental_cost(rental_days)
        self.late_fee = 0
        self.damage_charge = 0
        self.__paid = False   # Encapsulation

    def calculate_late_fee(self, actual_days):
        late_days = max(0, actual_days - self.rental_days)
        daily_penalty = self.vehicle.daily_rate * 0.20
        self.late_fee = daily_penalty * late_days
        return self.late_fee

    def calculate_total(self):
        return self.base_cost + self.late_fee + self.damage_charge

    def complete_rental(self, actual_days, damage_charge=0):
        if self.status != "ACTIVE":
            raise ValueError("Rental not active.")
        self.actual_days = actual_days
        self.damage_charge = damage_charge
        self.calculate_late_fee(actual_days)
        self.status = "COMPLETED"

    def mark_as_paid(self):
        if self.__paid:
            raise ValueError("Rental already paid.")
        self.__paid = True

    def is_paid(self):
        return self.__paid

    def display_rental_details(self):
        print("====================================")
        print("        SAFARIDRIVE RENTALS")
        print("====================================")
        print(f"Rental ID:        {self.rental_id}")
        print(f"Customer:         {self.customer.name}")
        print(f"Vehicle:          {self.vehicle.make} {self.vehicle.model}")
        print(f"Registration:     {self.vehicle.registration_number}")
        print(f"Rental Period:    {self.rental_days} days")
        print(f"Daily Rate:       KSh {self.vehicle.daily_rate}")
        print(f"Rental Charge:    KSh {self.base_cost}")
        if isinstance(self.vehicle, SUV):
            print("Service Charge:   KSh 2000")
        elif isinstance(self.vehicle, LuxuryCar):
            print(f"Insurance:        KSh {self.base_cost * 0.10}")
        print("------------------------------------")
        print(f"TOTAL:            KSh {self.calculate_total()}")
        print(f"Status:           {self.status}")
        print("====================================")
