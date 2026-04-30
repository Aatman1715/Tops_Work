# #Healthcare Industry
# Design a Python class ClinicAppointment that manages patient appointments in a clinic.
# The system should have the following features:
# Book Appointment:
# Prompt for patient name, age, mobile number, and preferred doctor.
# Show time slots (10am, 11am, 12pm, 2pm, 3pm).
# Check slot availability and confirm booking.
# View/Cancel Appointment:
# Allow patient to view or cancel their appointment using mobile number.
# Doctor Availability:
# Maintain a maximum of 3 appointments per time slot per doctor.
# Data Persistence:
# Store appointments in memory only (no files/dbs required)
class ClinicAppointment:
    def __init__(self):
        self.appointments = {}
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Lee"]

    def book_appointment(self):
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        mobile_number = input("Enter mobile number: ")
        doctor = input(f"Choose a doctor ({', '.join(self.doctors)}): ")
        
        if doctor not in self.doctors:
            print("Invalid doctor selection.")
            return
        
        print("Available time slots:")
        for slot in self.time_slots:
            print(slot)
        
        time_slot = input("Choose a time slot: ")
        
        if time_slot not in self.time_slots:
            print("Invalid time slot selection.")
            return
        
        # Check slot availability
        if doctor not in self.appointments:
            self.appointments[doctor] = {slot: [] for slot in self.time_slots}
        
        if len(self.appointments[doctor][time_slot]) < 3:
            self.appointments[doctor][time_slot].append({
                "name": name,
                "age": age,
                "mobile_number": mobile_number
            })
            print("Appointment booked successfully!")
        else:
            print("Selected time slot is fully booked for the chosen doctor.")

    def view_or_cancel_appointment(self):
        mobile_number = input("Enter your mobile number to view/cancel appointment: ")
        
        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for patient in patients:
                    if patient["mobile_number"] == mobile_number:
                        print(f"Appointment found with {doctor} at {slot}.")
                        action = input("Do you want to cancel this appointment? (yes/no): ")
                        if action.lower() == "yes":
                            patients.remove(patient)
                            print("Appointment cancelled successfully!")
                        return
        
        print("No appointment found with the provided mobile number.")
clinic = ClinicAppointment()
while True:
    print("\n1. Book Appointment")
    print("2. View/Cancel Appointment")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        clinic.book_appointment()
    elif choice == "2":
        clinic.view_or_cancel_appointment()
    elif choice == "3":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
