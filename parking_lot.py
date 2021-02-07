import sys
import os
import itertools
PATH = "{}".format(str(os.getcwd()))
FILENAME = 'input.txt'

class ParkingLot():

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__parking_spots = [ParkingSpot() for i in range(1,capacity+1)]
        print(f'Created a parking lot of {capacity} slots')

    def is_full(self):
        for spot in self.__parking_spots:
            if spot.is_vacant:
                return False
        return True

    def get_vacant_spots(self):
        return self.__vacant_spots

    def get_nearest_available_spot_id(self):
        for spot in self.__parking_spots:
            if spot.is_vacant():
                return spot.get_id()
    
    def allocate_spot(self, ticket):
        #spot doesn't exist 
        if self.is_full(): 
            print("Parking Full. Please wait for a spot to be empty")
            return 
        spot_id = self.get_nearest_available_spot_id()
        for spot in self.__parking_spots:
            if spot.get_id() == spot_id:
                spot.assign_ticket(ticket)
                break
        

    def free_spot(self, spot_id):
        for spot in self.__parking_spots:
            if spot.get_id() == spot_id:
                if spot.is_vacant():
                    print("Spot already vacant")
                    return
                spot.free()
                break

    def get_spot_by_registration_plate(self, reg_number):
        result = []
        for spot in self.__parking_spots:
            if spot.get_ticket()!= None and spot.get_ticket().get_license_number() == reg_number:
                result.append(spot.get_id())
        return result


    def get_spot_number_by_driver_age(self, age):
        result = []
        for spot in self.__parking_spots:
            if spot.get_ticket() != None and spot.get_ticket().get_driver_age() == age:
                result.append(spot.get_id())
        return result

    def get_registration_number_by_driver_age(self, age):
        result = []
        for spot in self.__parking_spots:
            if spot.get_ticket() != None and spot.get_ticket().get_driver_age() == age:
                result.append(spot.get_ticket().get_license_number())
        return result

    def get_spots(self):
        for spot in self.__parking_spots:
            print(spot)

    def __str__(self):
        return str(self.__parking_spots)



class ParkingSpot():

    id_iter = itertools.count(start=1)
    def __init__(self):
        self.__id = next(self.id_iter)
        self.__vacant = True
        self.__ticket = None

    def get_id(self):
        return self.__id

    def get_ticket(self):
        return self.__ticket

    def is_vacant(self):
        return self.__vacant
    
    def assign_ticket(self, ticket):
        self.__ticket = ticket
        self.__vacant = False
        print(f'Car with Vehicle Registration Number "{self.get_ticket().get_license_number()}"'\
            f'has been parked at slot number {self.__id}')

    def free(self):
        print(f'Slot number {self.__id} vacated,the car with registration number' \
                f'"{self.get_ticket().get_license_number()}" left the space.'\
                f' The driver of the car was of age {self.get_ticket().get_driver_age()}')
        self.__ticket = None
        self.__vacant = True
    
    def __repr__(self):
        return str(self.__id) + " " + str(self.is_vacant()) + " " 

class Ticket():
    def __init__(self, license_number, driver_age):
        self.__license_number = license_number
        self.__driver_age = driver_age

    def get_license_number(self):
        return self.__license_number

    def get_driver_age(self):
        return self.__driver_age

    def __str__(self):
        return str(self.license_number)


def take_input():
    print(os.getcwd())
    with open(FILENAME,'r') as f:
        content = f.readlines()
    
    content = [line.strip() for line in content]
    parking_lot = None
    ticket = None
    for line in content:
        if line.startswith("Create"):
            capacity = int(line[-1])
            parking_lot = ParkingLot(capacity)

        elif line.startswith("Park"):
            data = line.split()
            license_number = str(data[1])
            age = int(data[-1])
            ticket = Ticket(license_number, age)
            parking_lot.allocate_spot(ticket)

        elif line.startswith("Slot"):
            if "driver_of_age" in line:
                age = int(line.split()[1])
                print(parking_lot.get_spot_number_by_driver_age(age))

            elif "car_with_number" in line:
                number = line.split()[1]
                print(parking_lot.get_spot_by_registration_plate(number))

        elif line.startswith("Vehicle"):
            age = int(line.split()[1])
            print(parking_lot.get_registration_number_by_driver_age(age))

        elif line.startswith("Leave"):
            spot = int(line.split()[-1])
            parking_lot.free_spot(spot)

        else:
            print("Uh Oh! Are you sure the input file is correct? We couldn't recognize the command \
                from the set of given commands. Please check the input file and run again.")
        

if __name__ == '__main__':
    FILENAME = input("Enter file name for input : ") or FILENAME
    take_input()










