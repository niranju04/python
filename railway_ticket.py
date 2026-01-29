trains = {
    "Express": 5,
    "Intercity": 3,
    "Superfast": 4
}

def view_trains():
    print("\nAvailable Trains")
    for train, seats in trains.items():
        print(train, " Seats:", seats)


def book_ticket():
    name = input("Enter passenger name: ")
    train = input("Enter train name: ")

    if train in trains:
        if trains[train] > 0:
            trains[train] -= 1

            file = open("tickets.txt", "a")
            file.write(name + "," + train + "\n")
            file.close()

            print("Ticket booked successfully")
        else:
            print("No seats available")
    else:
        print("Train not found ")


def cancel_ticket():
    name = input("Enter passenger name: ")
    train = input("Enter train name: ")

    updated = []
    found = False

    try:
        file = open("tickets.txt", "r")
        for line in file:
            p_name, t_name = line.strip().split(",")
            if p_name == name and t_name == train and not found:
                trains[train] += 1
                found = True
                print("Ticket cancelled successfully ")
            else:
                updated.append(line)
        file.close()

        file = open("tickets.txt", "w")
        file.writelines(updated)
        file.close()

        if not found:
            print("Ticket not found")

    except FileNotFoundError:
        print("No bookings ")


while True:
    print("\n Railway Ticket Booking ")
    print("1. View Trains")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_trains()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        cancel_ticket()
    elif choice == "4":
        print("Happy Journey ")
        break
    else:
        print("Invalid choice ")
