# Design a Python class BusReservation that simulates a basic bus ticket booking system.
# Features should include:
# Show Available Routes:
# Predefined city routes with fixed prices.
# Example: "Mumbai to Pune - ₹500"
# "Delhi to Jaipur - ₹600"
# , etc.
# Book Ticket:
# Enter passenger name, age, mobile, and route.
# Assign seat number (max 40 per bus per route).
# Generate a unique ticket ID.
# View Ticket:
# Cancel Ticket:
# Lookup using ticket ID.
# Cancel the ticket if it exists.
# Exit
class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 700
        }
        self.tickets = {}
        self.next_ticket_id = 1

    def show_available_routes(self):
        print("Available Routes:")
        for route, price in self.routes.items():
            print(f"{route} - ₹{price}")

    def book_ticket(self):
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        mobile = input("Enter mobile number: ")
        
        print("Available Routes:")
        for route in self.routes.keys():
            print(route)
        
        route = input("Choose a route: ")
        
        if route not in self.routes:
            print("Invalid route selection.")
            return
        
        # Check seat availability
        if route not in self.tickets:
            self.tickets[route] = []
        
        if len(self.tickets[route]) < 40:
            ticket_id = self.next_ticket_id
            self.tickets[route].append({
                "ticket_id": ticket_id,
                "name": name,
                "age": age,
                "mobile": mobile
            })
            self.next_ticket_id += 1
            print(f"Ticket booked successfully! Your ticket ID is {ticket_id}.")
        else:
            print("No seats available for the selected route.")

    def view_ticket(self):
        ticket_id = int(input("Enter ticket ID to view details: "))
        
        for route, tickets in self.tickets.items():
            for ticket in tickets:
                if ticket["ticket_id"] == ticket_id:
                    print(f"Ticket ID: {ticket['ticket_id']}")
                    print(f"Name: {ticket['name']}")
                    print(f"Age: {ticket['age']}")
                    print(f"Mobile: {ticket['mobile']}")
                    print(f"Route: {route}")
                    return
        
        print("Ticket ID not found.")

    def cancel_ticket(self):
        ticket_id = int(input("Enter ticket ID to cancel: "))
        
        for route, tickets in self.tickets.items():
            for i, ticket in enumerate(tickets):
                if ticket["ticket_id"] == ticket_id:
                    del tickets[i]
                    print("Ticket cancelled successfully.")
                    return
        
        print("Ticket ID not found.")
reservation_system = BusReservation()
while True:
    print("\n1. Show Available Routes")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        reservation_system.show_available_routes()
    elif choice == "2":
        reservation_system.book_ticket()
    elif choice == "3":
        reservation_system.view_ticket()
    elif choice == "4":
        reservation_system.cancel_ticket()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")