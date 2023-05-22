# eligblePassengers = []
# notEligblePassengers = []
# for i in range(1, 4):
#     ticketClass = str(input("Enter ticket class: First Class (F), Business Class (B), Economy Class (E):"))
#     ticketNum = int(input("Enter ticket number: "))
#     weight = int(input("Enter weight: "))
#     if ticketClass == "F":
#         if weight <= 25:
#             print("You can board")
#             eligblePassengers.append([ticketNum, weight])

#         else:
#             print("You cannot board")
#             notEligblePassengers.append([ticketNum, weight])
#     elif ticketClass == "B":
#         if weight <=30:
#             print("You can board")
#             eligblePassengers.extend([ticketNum, weight])
#         else:
#             print("You cannot board")
#             notEligblePassengers.append([ticketNum, weight])
#     elif ticketClass == "E":
#         if weight <= 15:
#             print("You can board")
#             eligblePassengers.append([ticketNum, weight])
#         else:
#             print("You cannot board")
#             notEligblePassengers.append([ticketNum, weight])
#     else:
#         print("Invalid ticket class. Try again")
# print("Eligible passengers: Passenger ID %d and the luggage weight of the passenger %d", eligblePassengers)
# print("Eligible passengers: Passenger ID %d and the luggage weight of the passenger %d", notEligblePassengers)


# fixed code 
eligible_passengers = []
not_eligible_passengers = []

for i in range(1, 4):
    ticket_class = str(input("Enter ticket class: First Class (F), Business Class (B), Economy Class (E): "))
    ticket_number = int(input("Enter ticket number: "))

    if ticket_class == "F":
        weight = int(input("Enter weight between 1-25: "))
        if weight <= 25:
            print("You can board.")
            eligible_passengers.append([ticket_number, weight])
        else:
            print("You cannot board.")
            not_eligible_passengers.append([ticket_number, weight])
    elif ticket_class == "B":
        weight = int(input("Enter weight between 1-30: "))
        if weight <= 30:
            print("You can board.")
            eligible_passengers.append([ticket_number, weight])
        else:
            print("You cannot board.")
            not_eligible_passengers.append([ticket_number, weight])
    elif ticket_class == "E":
        weight = int(input("Enter weight between 1-15: "))
        if weight <= 15:
            print("You can board.")
            eligible_passengers.append([ticket_number, weight])
        else:
            print("You cannot board.")
            not_eligible_passengers.append([ticket_number, weight])
    else:
        print("Invalid ticket class. Try again.")

print("Eligible passengers:")
for passenger in eligible_passengers:
    print("Passenger ID {} and the luggage weight of the passenger {}".format(passenger[0], passenger[1]))

print("Not eligible passengers:")
for passenger in not_eligible_passengers:
    print("Passenger ID {} and the luggage weight of the passenger {}".format(passenger[0], passenger[1]))


