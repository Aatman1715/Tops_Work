#Code to store car details like brand, model, type of fuel used, mileage, 
# year and price of the car in a nested dictionary and print the details. Also user should be 
# able to search for a car by its brand and model and display the details of the car if found.

cars = {
    "Toyota": {
        "Camry": {
            "fuel": "Gasoline",
            "mileage": "28 MPG",
            "year": 2020,
            "price": "$24,000"
        },
        "Corolla": {
            "fuel": "Gasoline",
            "mileage": "30 MPG",
            "year": 2021,
            "price": "$20,000"
        }
    },
    "Honda": {
        "Civic": {
            "fuel": "Gasoline",
            "mileage": "32 MPG",
            "year": 2019,
            "price": "$22,000"
        },
        "Accord": {
            "fuel": "Gasoline",
            "mileage": "29 MPG",
            "year": 2020,   
            "price": "$25,000"
        }
    }
}
def search_car(brand, model):
    if brand in cars and model in cars[brand]:
        details = cars[brand][model]
        return f"Brand: {brand}, Model: {model}, Fuel: {details['fuel']}, Mileage: {details['mileage']}, Year: {details['year']}, Price: {details['price']}"
    else:
        return "Car not found."
brand = input("Enter the car brand: ")
model = input("Enter the car model: ")
result = search_car(brand, model)
print(result)
