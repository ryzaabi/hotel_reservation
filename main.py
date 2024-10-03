class Customer:
    def __init__(self,customer_id,name,email,phone_number,address):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._address = address

    # Getter and setter methods
    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self,customer_id):
        self._customer_id = customer_id

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self,email):
        self._email = email

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self,phone_number):
        self._phone_number = phone_number

    def get_address(self):
        return self._address

    def set_address(self,address):
        self._address = address

    # Other required functions
    def make_reservation(self):
        pass  # Logic to make a reservation

    def view_reservation(self):
        pass  # Logic to view a reservation

    def modify_reservation(self,reservation_id):
        pass  # Logic to modify an existing reservation

    def cancel_reservation(self,reservation_id):
        pass  # Logic to cancel a reservation

class Reservation:
    def __init__(self,reservation_id,customer_id,room_id,check_in_date,check_out_date,status):
        self._reservation_id = reservation_id
        self._customer_id = customer_id
        self._room_id = room_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._status = status

    # Getter and setter methods
    def get_reservation_id(self):
        return self._reservation_id

    def set_reservation_id(self,reservation_id):
        self._reservation_id = reservation_id

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self,customer_id):
        self._customer_id = customer_id

    def get_room_id(self):
        return self._room_id

    def set_room_id(self,room_id):
        self._room_id = room_id

    def get_check_in_date(self):
        return self._check_in_date

    def set_check_in_date(self,check_in_date):
        self._check_in_date = check_in_date

    def get_check_out_date(self):
        return self._check_out_date

    def set_check_out_date(self,check_out_date):
        self._check_out_date = check_out_date

    def get_status(self):
        return self._status

    def set_status(self,status):
        self._status = status

    # Other required functions
    def confirm(self):
        pass  # Logic to confirm a reservation

    def cancel(self):
        pass  # Logic to cancel a reservation

    def modify(self):
        pass  # Logic to modify a reservation
class Room:
    def __init__(self,room_id,room_type,price,availability,amenities):
        self._room_id = room_id
        self._room_type = room_type
        self._price = price
        self._availability = availability
        self._amenities = amenities

    # Getter and setter methods
    def get_room_id(self):
        return self._room_id

    def set_room_id(self,room_id):
        self._room_id = room_id

    def get_room_type(self):
        return self._room_type

    def set_room_type(self,room_type):
        self._room_type = room_type

    def get_price(self):
        return self._price

    def set_price(self,price):
        self._price = price

    def is_available(self):
        return self._availability

    def set_availability(self,availability):
        self._availability = availability

    def get_amenities(self):
        return self._amenities

    def set_amenities(self,amenities):
        self._amenities = amenities

    # Other required functions
    def check_availability(self):
        pass  # Logic to check room availability

    def get_room_details(self):
        pass  # Logic to return room details

class Hotel:
    def __init__(self,hotel_id,name,location,rooms):
        self._hotel_id = hotel_id
        self._name = name
        self._location = location
        self._rooms = rooms  # This should be a list of Room objects

    # Getter and setter methods
    def get_hotel_id(self):
        return self._hotel_id

    def set_hotel_id(self,hotel_id):
        self._hotel_id = hotel_id

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_location(self):
        return self._location

    def set_location(self,location):
        self._location = location

    def get_rooms(self):
        return self._rooms

    def set_rooms(self,rooms):
        self._rooms = rooms

    # Other required functions
    def search_available_rooms(self,check_in,check_out):
        pass  # Logic to search available rooms

    def filter_rooms(self,criteria):
        pass  # Logic to filter rooms based on criteria

# Creating Customer objects
customer_rashed = Customer(customer_id=1,name="Rashed",email="rashed@gmail.com",phone_number="1234567890",address="Abu Dhabi,UAE")
customer_mohamed = Customer(customer_id=2,name="Mohamed",email="mohamed@gmail.com",phone_number="0987654321",address="Dubai,UAE")
customer_zayed = Customer(customer_id=3,name="Zayed",email="zayed@gmail.com",phone_number="1122334455",address="Sharjah,UAE")

# Creating Room objects
room_burj_al_arab = Room(room_id=101,room_type="2 Queen Beds /No Smoking",price=899.95,availability=True,amenities=["Desk","Safe","Coffee Maker","Hair Dryer"])
room_bab_al_qasr = Room(room_id=102,room_type="1 King Bed /Non Smoking",price=1099.95,availability=True,amenities=["Jacuzzi","Mini Bar","Safe","Smart TV"])

# Creating Hotel objects
hotel_burj_al_arab = Hotel(hotel_id=1,name="Burj Al Arab",location="Dubai,UAE",rooms=[room_burj_al_arab])
hotel_bab_al_qasr = Hotel(hotel_id=2,name="Bab Al Qasr",location="Abu Dhabi,UAE",rooms=[room_bab_al_qasr])

# Creating Reservation objects for the customers
reservation_rashed = Reservation(reservation_id=1001,customer_id=customer_rashed.get_customer_id(),room_id=room_burj_al_arab.get_room_id(),check_in_date="2024-10-01",check_out_date="2024-10-03",status="Confirmed")
reservation_mohamed = Reservation(reservation_id=1002,customer_id=customer_mohamed.get_customer_id(),room_id=room_bab_al_qasr.get_room_id(),check_in_date="2024-10-05",check_out_date="2024-10-07",status="Confirmed")
reservation_zayed = Reservation(reservation_id=1003,customer_id=customer_zayed.get_customer_id(),room_id=room_burj_al_arab.get_room_id(),check_in_date="2024-10-10",check_out_date="2024-10-12",status="Confirmed")

# Displaying the reservation details
def display_reservation(reservation,customer,room,hotel):
    print("Your Reservation Is Confirmed")
    print(f"Your Name: {customer.get_name()}")
    print(f"Your Email: {customer.get_email()}")
    print(f"Hotel: {hotel.get_name()}")
    print(f"Room Type: {room.get_room_type()}")
    print(f"Check-In: {reservation.get_check_in_date()}")
    print(f"Check-Out: {reservation.get_check_out_date()}")
    print(f"Number of Nights: {(int(reservation.get_check_out_date().split('-')[2]) - int(reservation.get_check_in_date().split('-')[2]))}")
    print(f"Room Price: ${room.get_price()}")
    print(f"Total Charges: ${(room.get_price()) * (int(reservation.get_check_out_date().split('-')[2]) - int(reservation.get_check_in_date().split('-')[2]))}")
    print("-" * 50)

# Displaying reservations for each customer
display_reservation(reservation_rashed,customer_rashed,room_burj_al_arab,hotel_burj_al_arab)
display_reservation(reservation_mohamed,customer_mohamed,room_bab_al_qasr,hotel_bab_al_qasr)
display_reservation(reservation_zayed,customer_zayed,room_burj_al_arab,hotel_burj_al_arab)

