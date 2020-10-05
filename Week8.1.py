import logging     #to import logging

logging.basicConfig(filename="goodies.py, level = logging.INFO")
with open("goodies.py") as f:
    read_data = f.read()

filename = input ("filename: ")
with open(filename, "w") as f:
    f.write(input(full_name , address, phone_number))
    full_name = "what is your name?"
    address = "What is your address?"
    phone_number = "What is your 10 digit phone number?"

