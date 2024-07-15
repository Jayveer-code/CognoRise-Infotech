import random
import string
def task2():
    # Prompt user for the length of the password
    password_length = int(input("Enter the desired length of the password: ")) 
    
    # Define the set of possible characters
    format = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    generated_password = ''.join(random.choice(format) for _ in range(password_length))
    
    # Print the generated password
    print(f"Generated Password ==> {generated_password}")

# Call the function to generate and display the password
task2()


