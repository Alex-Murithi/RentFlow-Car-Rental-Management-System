# customer.py

class Customer:
    def __init__(self, customer_id, name, phone_number, national_id, driving_licence):
        if not driving_licence:
            raise ValueError("Customer must have a driving licence.")
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.driving_licence = driving_licence
        self.rentals = []   # list of Rental objects

    def display_details(self):
        print(f"Customer {self.customer_id}: {self.name}, Phone: {self.phone_number}")

    def add_rental(self, rental):
        self.rentals.append(rental)

    def view_rental_history(self):
        if not self.rentals:
            print(f"{self.name} has no rental history.")
        else:
            print(f"Rental history for {self.name}:")
            for r in self.rentals:
                r.display_rental_details()
