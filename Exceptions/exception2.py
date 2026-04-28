#Create a exception called PasswordValidationError
#Lenght of password should be greater than 6 characters
#Password should contain at least one uppercase letter, one lowercase letter, and one digit, special character
#If the password is valid, print "Password is valid".
class PasswordValidationError(Exception):
    pass                        
def validate_password(password):
    if len(password) <= 6:
        raise PasswordValidationError("Password must be greater than 6 characters.")
    if not any(char.isupper() for char in password):
        raise PasswordValidationError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise PasswordValidationError("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        raise PasswordValidationError("Password must contain at least one digit.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        raise PasswordValidationError("Password must contain at least one special character.")
    print("Password is valid.")
try:
    user_password = input("Enter your password: ")
    validate_password(user_password)
except PasswordValidationError as e:
    print(f"Password validation error: {e}")    
