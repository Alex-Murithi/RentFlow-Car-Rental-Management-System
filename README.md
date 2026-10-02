RentFlow – Car Rental Management System
__Overview__
RentFlow is a Python OOP capstone project simulating SafariDrive Rentals.
It demonstrates all four pillars of Object-Oriented Programming (OOP):

Abstraction → Abstract `Vehicle` and `Payment` classes define required behaviors.

Inheritance → `EconomyCar`, `SUV`, `LuxuryCar` reuse `Vehicle`; payment types reuse Payment.

Polymorphism → `calculate_rental_cost()` and `process_payment()` behave differently depending on subclass.

Encapsulation → Private attributes (`__available`, `__paid`, `__revenue`) protect critical data.

The system manages vehicles, customers, rentals, payments, returns, late fees, and revenue tracking.

__Project Structure__

rentflow/
│
├── main.py            # Demo run
├── vehicle.py         # Vehicle classes
├── customer.py        # Customer class
├── rental.py          # Rental lifecycle
├── payment.py         # Payment types
├── rental_system.py   # CarRentalSystem manager
└── README.md
__Features__
Register customers with ID, phone, national ID, and driving licence.

Add vehicles (Economy, SUV, Luxury) with pricing rules.

Rent and return vehicles, with late fees and damage charges.

Process payments via M-Pesa, Card, or Cash.

Track revenue securely.

Generate management reports with fleet and rental statistics.

__Business Rules__
Daily rates cannot be negative.

Customers must have a driving licence.

Vehicles must be in the fleet before renting.

Rental days must be greater than zero.

A rented vehicle cannot be rented again until returned.

Payments happen only once, after rental completion.

__Conclusion__
RentFlow is a complete OOP-driven car rental management system.
It demonstrates clean design, modular code, and practical application of OOP principles in Python.