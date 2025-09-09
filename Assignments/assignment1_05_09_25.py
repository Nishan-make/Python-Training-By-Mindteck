# Assignment using python:
 
# Problem Statement
# You are asked to design a Flight Management System in Python using exception handling.
 
# The system should:
# - Read flight information from a file called flights.txt.
# - Each line has: flight_number available_seats price_per_ticket
#   Example: AI101 50 6000
 
# Ask the user for:
# - Flight number
# - Number of tickets to book
 
# Implement the following exception rules: (Questions below)
 
# (a) Raise FlightNotFoundError (custom) if the entered flight number does not exist.
 
# (b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
 
# (c) Handle ValueError if user enters invalid input (like string instead of integer).
 
# (d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket).
 
# (e) Always close the file using finally.
 
# The program should print:
# - Flight details
# - Total booking cost
# - Discount per ticket (total / tickets)
 
# Note**:
# Use nested try-except:
 
# Inner block for booking operations.
 
# # Outer block for file handling & re-raised exceptions
# ===================================================================================

# Custom Exceptions
class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass

def read_flights_file(filename):
    flights = {}
    f = None
    try:
        f = open(filename, "r")
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                flight_number, seats, price = parts
                flights[flight_number] = {
                    "available_seats": int(seats),
                    "price_per_ticket": float(price)
                }
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    finally:
        if f:
            f.close()
            print("File closed.")
    return flights

def book_flight(flights):
    try:
        flight_number = input("Enter flight number: ").strip().upper()
        if flight_number not in flights:
            raise FlightNotFoundError(f"Flight {flight_number} not found.")

        try:
            tickets = int(input("Enter number of tickets to book: "))

            if tickets <= 0:
                raise ZeroDivisionError("Number of tickets cannot be zero or negative.")

            flight = flights[flight_number]
            if tickets > flight["available_seats"]:
                raise SeatsUnavailableError("Not enough seats available.")

            total_cost = tickets * flight["price_per_ticket"]
            discount_per_ticket = total_cost / tickets  # Can raise ZeroDivisionError if tickets == 0

            # Print booking info
            print("\n--- Booking Confirmed ---")
            print(f"Flight: {flight_number}")
            print(f"Available Seats: {flight['available_seats']}")
            print(f"Price per Ticket: ₹{flight['price_per_ticket']}")
            print(f"Tickets Booked: {tickets}")
            print(f"Total Cost: ₹{total_cost}")
            print(f"Discount per Ticket (for simulation): ₹{discount_per_ticket:.2f}")

        except ValueError:
            print("Invalid input. Please enter numeric values for tickets.")
        except ZeroDivisionError as zde:
            print("Error:", zde)
        except SeatsUnavailableError as sue:
            print("Error:", sue)

    except FlightNotFoundError as fne:
        print("Error:", fne)

# Main Program
def main():
    flights = read_flights_file("flights.txt")
    if flights:
        book_flight(flights)

if __name__ == "__main__":
    main()
