class Flight():
    def __init__(self, capacity) :
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False 
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity -  len(self.passengers)

flight = Flight(2)

people = ["Ana", "Bia", "Kened", "Kevin"]

for person in people:
    if flight.add_passenger(person): 
        print(f"Added {person} to the flight sucessfully!")
    else:
        print(f"No avaliable seats for {person}")