

from abc import ABC, abstractmethod
import uuid


class Passenger(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def name(self):
        return self.__name

    def age(self):
        return self.__age

    @abstractmethod
    def get_discount(self):
        pass



class RegularPassenger(Passenger):
    def get_discount(self):
        return 10


class StudentPassenger(Passenger):
    def get_discount(self):
        return 20



class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def display(self):
        print(
            f"{self.code:<10}{self.airline:<15}"
            f"{self.source:<15}{self.destination:<15}"
            f"{self.seats:<10}Rs.{self.fare}"
        )



class Booking:
    def __init__(self, passenger, flight, tickets):
        self.booking_id = str(uuid.uuid4())[:8].upper()
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets

        self.base_fare = flight.fare * tickets
        self.discount = (
            self.base_fare * passenger.get_discount() / 100
        )
        self.total_fare = self.base_fare - self.discount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID        :", self.booking_id)
        print("Passenger Name    :", self.passenger.name())
        print("Passenger Age     :", self.passenger.age())
        print("Passenger Category:", type(self.passenger).__name__)
        print("Flight Code       :", self.flight.code)
        print("Airline           :", self.flight.airline)
        print("Source            :", self.flight.source)
        print("Destination       :", self.flight.destination)
        print("Number of Tickets :", self.tickets)
        print("Base Fare         : Rs.", self.base_fare)
        print("Discount          : Rs.", self.discount)
        print("Final Amount      : Rs.", self.total_fare)
        print("======================================")



class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("AI101", "Air India", "Delhi", "Mumbai", 100, 5000),
            Flight("6E202", "IndiGo", "Mumbai", "Bangalore", 40, 4000),
            Flight("SG303", "SpiceJet", "Delhi", "Chennai", 30, 4500)
        ]

        self.bookings = []

    
    def view_flights(self):
        print("\n========== AVAILABLE FLIGHTS ==========")
        print(
            f"{'Code':<10}{'Airline':<15}{'Source':<15}"
            f"{'Destination':<15}{'Seats':<10}{'Fare'}"
        )
        print("-" * 80)

        for flight in self.flights:
            flight.display()

    
    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight

        return None

    
    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Error: Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()

        if not name or not all(
            part.isalpha() for part in name.split()
        ):
            print("Error: Enter a valid passenger name.")
            return

        try:
            age = int(input("Enter passenger age: "))

            if age < 1 or age > 120:
                print("Error: Age must be between 1 and 120.")
                return

            tickets = int(input("Enter number of tickets: "))

            if tickets < 1:
                print("Error: At least one ticket is required.")
                return

            if tickets > flight.seats:
                print("Error: Not enough seats available.")
                return

        except ValueError:
            print("Error: Enter valid numbers for age and tickets.")
            return

        print("\nPassenger Category:")
        print("1. Regular Passenger (10% discount)")
        print("2. Student Passenger (20% discount)")

        category = input("Enter choice: ").strip()

        if category == "1":
            passenger = RegularPassenger(name, age)

        elif category == "2":
            passenger = StudentPassenger(name, age)

        else:
            print("Error: Invalid passenger category.")
            return

        booking = Booking(passenger, flight, tickets)

        flight.seats -= tickets
        self.bookings.append(booking)

        print("\nBooking confirmed successfully!")
        booking.display_summary()

    
    def view_booking(self):
        if not self.bookings:
            print("\nNo confirmed bookings found.")
            return

        print("\nMost Recent Confirmed Booking:")
        self.bookings[-1].display_summary()

    
    def run(self):
        while True:
            print("\n========== FLIGHT BOOKING SYSTEM ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using Flight Booking System!")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()