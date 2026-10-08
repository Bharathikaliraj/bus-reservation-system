# BUS RESERVATION SYSTEM

from_place = input("Enter From Place: ")
to_place = input("Enter To Place: ")
journey_date = input("Enter Journey Date: ")

print("\nAvailable Buses")
print("1. KPN Travels")
print("2. SRM Travels")
print("3. Parveen Travels")

choice = int(input("Select Bus (1-3): "))

if choice == 1:
    bus_name = "KPN Travels"
elif choice == 2:
    bus_name = "SRM Travels"
elif choice == 3:
    bus_name = "Parveen Travels"
else:
    bus_name = "Invalid Option"

print("Selected Bus:", bus_name)


# BUS DETAILS

buses = {
    1: {
        "bus_name": "KPN Travels",
        "departure": "09:00 PM",
        "pickup": "Chennai CMBT",
        "drop": "Coimbatore Gandhipuram",
        "arrival": "05:30 AM",
        "price": 850
    },

    2: {
        "bus_name": "SRM Travels",
        "departure": "10:00 PM",
        "pickup": "Chennai Koyambedu",
        "drop": "Coimbatore Ukkadam",
        "arrival": "06:00 AM",
        "price": 900
    },

    3: {
        "bus_name": "Parveen Travels",
        "departure": "09:00 PM",
        "pickup": "Chennai Koyambedu",
        "drop": "Coimbatore Gandhipuram",
        "arrival": "05:30 AM",
        "price": 850
    }
}


def show_bus_details(bus_no):
    bus = buses[bus_no]

    print("\n------ Bus Details ------")
    print("Bus Name:", bus["bus_name"])
    print("Departure:", bus["departure"])
    print("Pickup:", bus["pickup"])
    print("Drop:", bus["drop"])
    print("Arrival:", bus["arrival"])
    print("Ticket Price:", bus["price"])


show_bus_details(choice)


# SEAT BOOKING

seats = list(range(1, 21))
booked_seats = []


def booking():
    print("\nAvailable Seats:", seats)

    count = int(input("How many seats do you want to book? "))

    for i in range(count):
        seat = int(input("Enter Seat Number: "))

        try:
            seats.remove(seat)
            booked_seats.append(seat)

            print("Seat", seat, "Booked Successfully")

        except ValueError:
            print("Seat", seat, "Already Booked")


booking()


# CANCELLATION

def cancellation():

    print("\nBooked Seats:", booked_seats)

    cancel = input(
        "Do you want to cancel the seat? (yes/no): "
    ).lower()

    if cancel == "yes":

        count = int(
            input("How many seats do you want to cancel? ")
        )

        for i in range(count):

            seat = int(
                input("Enter Seat Number to Cancel: ")
            )

            if seat in booked_seats:

                booked_seats.remove(seat)
                seats.append(seat)
                seats.sort()

                print(
                    "Seat",
                    seat,
                    "Cancelled Successfully"
                )

            else:

                print(
                    "Seat",
                    seat,
                    "is Not Booked"
                )

    else:
        print("Cancellation skipped")


print("\n--- Cancellation ---")
cancellation()


print("\nAvailable Seats:", seats)
print("Booked Seats:", booked_seats)


# PASSENGER DETAILS

def passenger_details():
    global passengers, phone, pickup, drop

    print("\n--- Passenger Details ---")

    phone = input("Enter Phone Number: ")
    pickup = input("Enter Pickup Place: ")
    drop = input("Enter Drop Place: ")

    passengers = []

    count = len(booked_seats)

    for i in range(count):

        print("\nPassenger", i + 1)

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")

        passenger = {
            "name": name,
            "age": age,
            "gender": gender
        }

        passengers.append(passenger)



    print("\n--- Passenger Details ---")

    for i in range(len(passengers)):

        print("Passenger", i + 1)
        print("Name:", passengers[i]["name"])
        print("Age:", passengers[i]["age"])
        print("Gender:", passengers[i]["gender"])

    print("Phone:", phone)
    print("Pickup:", pickup)
    print("Drop:", drop)


passenger_details()


# PAYMENT

def payment(booked_seats, price):

    print("\n--- Payment ---")

    total = 0

    for seat in booked_seats:

        print("Seat", seat, ":", "₹", price)

        total = total + price

    print("\nTotal Amount: ₹", total)

    print("\n1. Cash")
    print("2. UPI")
    print("3. Card")

    payment_choice = int(
        input("Select Payment Method: ")
    )

    if payment_choice == 1:

        print("Payment Method: Cash")

    elif payment_choice == 2:

        print("Payment Method: UPI")

    elif payment_choice == 3:

        print("Payment Method: Card")

    else:

        print("Invalid Payment Method")
        return

    print("Payment Successful")


# SELECTED BUS PRICE

price = buses[choice]["price"]

payment(booked_seats, price)



# PRINT TICKET

def print_ticket():

    print("\n==============================")
    print("          BUS TICKET")
    print("==============================")

    for i in range(len(booked_seats)):

        print("Passenger", i + 1)
        print("Name   :", passengers[i]["name"])
        print("Age    :", passengers[i]["age"])
        print("Gender :", passengers[i]["gender"])
        print("Seat   :", booked_seats[i])
        print("Phone  :", phone)
        print("Pickup :", pickup)
        print("Drop   :", drop)
        print("Bus    :", buses[choice]["bus_name"])
        print("Date   :", journey_date)
        print("------------------------------")
    total = buses[choice]["price"] * len(booked_seats)

    print("Total  : ₹", total)

    print("==============================")
    print("     BOOKING SUCCESSFUL")
    print("==============================")


# FUNCTION CALL

print_ticket()
