#====================================== Number 1======================================
# Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
# Requirements:
# -Flight should have attributes: flight number, airline.
# -ScheduledFlight should add departure time and arrival time.
# -Include methods to display complete flight information.

# Base Class
class Flight:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline

    def display_info(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")

# Derived Class
class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, departure_time, arrival_time):
        super().__init__(flight_number, airline)
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def display_info(self):
        print("All information about the Flight -")
        super().display_info()
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Time: {self.arrival_time}")

#============================================ Number 2 =====================================================
# Create a base class Person, derived class CrewMember, and a further derived class Pilot.
# -Person contains name and ID.
# -CrewMember adds role (e.g., "Cabin Crew", "Pilot").
# -Pilot adds license number and rank (e.g., "Captain").

# Base Class
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.person_id}")

# Derived Class
class CrewMember(Person):
    def __init__(self, name, person_id, role):
        super().__init__(name, person_id)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

# Further Derived Class
class Pilot(CrewMember):
    def __init__(self, name, person_id, license_number, rank, role):
        super().__init__(name, person_id, role)
        self.license_number = license_number
        self.rank = rank

    def display_info(self):
        super().display_info()
        print(f"License Number: {self.license_number}")
        print(f"Rank: {self.rank}")

#====================================== Number 3 ==================================================
# Create a base class Service, and derive two classes: SecurityService and BaggageService.
# Requirements:
# -Service class has a method service_info().
# -Derived classes override or extend this to describe their own service.

# Base Class
class Service:
    def service_info(self):
        print("General Airport Service")

# Derived Class
class SecurityService(Service):
    def service_info(self):
        print("Security Check and Passenger Screening")

# Derived Class
class BaggageService(Service):
    def service_info(self):
        print("Baggage Handling and Delivery")


#======================================== Number 4 ==================================================
# Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
# Requirements:
# - PassengerDetails has name, age.
# - TicketDetails has ticket number, seat number.
# - Booking shows all information.

# Base Class 1
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Base Class 2
class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

# Multiple Inheritance Class
class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def display_booking(self):
        print(f"Passenger Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Seat Number: {self.seat_number}")


# Test ScheduledFlight
sf = ScheduledFlight("AI202", "Emirates", "09:00 AM", "12:00 PM")
sf.display_info()
print("\n*****************************\n")

# Test Services
security = SecurityService()
baggage = BaggageService()

security.service_info()
baggage.service_info()
print("\n***************************\n")

# Test Pilot
pilot = Pilot("Suresh Bhatt", "S23455", "LN56789", "C55", "Captain")
pilot.display_info()
print("\n***********************\n")

# Test Booking
booking = Booking("Suranjan Dutta", 30, "TK1234", "12A")
booking.display_booking()
