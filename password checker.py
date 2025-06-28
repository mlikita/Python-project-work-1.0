# Password strength checker

import re 

# conditions:
# min 8 characters,digits,uppercase,lowercase and special characters

def check_password_strength(password):
    if len(password)<8:
        return "Weak:Password must contain atleast 8 characters"
    
    if not any(char.isdigit() for char in password):
        return "Weak:Password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak:Password must contain a upper character"

    if not any(char.islower() for char in password):
        return "Weak: Password must contain a lower character"
    
    if not re.search(r'[!@#$%^&*(){}<>,.?]',password):
        return "Medium:Password must contain a special character"
    
    return "Strong:Your password is secure!"

def Password_checker():
    print("Welcome! to the password strength checker")

    while True:
        password=input("Enter your password (or type 'exit' or quit): ")

        # if password.lower() in ['exit' or 'quit']:
        if password.lower() =='exit':
            print("Thank you for using this tool")
            break
        result=check_password_strength(password)
        print(result)

# run the password checker tool

if __name__=="__main__":#it will execute first
    Password_checker()




