# Class for System Admin
class SystemAdmin:
    def __init__(self, ID, name, tel_no, address):
        self.ID = ID
        self.name = name
        self.tel_no = tel_no
        self.address = address

    def update_rooms(self):
        print("Updating rooms...")

    def manage_inventory(self):
        print("Managing inventory...")


# Class for Receptionist
class Receptionist:
    def __init__(self, ID, name, tel_no, address):
        self.ID = ID
        self.name = name
        self.tel_no = tel_no
        self.address = address

    def checkin(self, customer, room):
        print(f"{customer.name} checked into room {room.room_no}")

    def checkout(self, customer, room):
        print(f"{customer.name} checked out from room {room.room_no}")

    def generate_bill(self, customer, amount):
        bill = Bill(customer.ID, customer.name, amount)
        return bill

    def reserve_room(self, room):
        print(f"Room {room.room_no} reserved.")

    def create_account(self, customer):
        print(f"Account created for customer: {customer.name}")


# Class for Rooms
class Rooms:
    def __init__(self, room_no, status="Available"):
        self.room_no = room_no
        self.status = status

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


# Class for Customer
class Customer:
    def __init__(self, ID, name, tel_no, address):
        self.ID = ID
        self.name = name
        self.tel_no = tel_no
        self.address = address

    def pay_bill(self, bill):
        print(f"{self.name} paid {bill.amount}")

    def book_room(self, room):
        print(f"{self.name} booked room {room.room_no}")

    def create_account(self):
        print(f"Account created for customer: {self.name}")


# Class for Bill
class Bill:
    def __init__(self, bill_no, customer_name, amount):
        self.bill_no = bill_no
        self.customer_name = customer_name
        self.amount = amount

    def __str__(self):
        return f"Bill No: {self.bill_no}, Customer: {self.customer_name}, Amount: {self.amount}"


# Sample usage
admin = SystemAdmin(1, "Shakur", "123456789", "North road")
receptionist = Receptionist(1, "Adil", "987654321", "North road")
customer = Customer(1, "Shakur_D", "111222333", "North road")
room = Rooms(101)
bill = receptionist.generate_bill(customer, 500)
customer.pay_bill(bill)
