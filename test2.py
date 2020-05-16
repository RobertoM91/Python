import os
import json

print("Welcome to my file processor.")
print("Let's build your profile.")

print("Great! Thank you for information!")


def check_path():
	if os.path.isdir(path):
		print("Great! This path exists!")
	else:
		print("Sorry, this path does not exist.")

def create_file():
	name = input("What is your name: ")
	address = input("What is your address: ")
	phone_number = input("What is your phone number: ")
	with open(completepath, 'w') as filehandle:
		filehandle.write(name+','+address+','+phone_number+'\n')
		filehandle.close()

def show_file():
	with open(completepath, 'r') as filehandle:
		data = filehandle.read()		
		print(data)

path = input("Please enter a path directory. Mine is /RobertoM91/Python/")
check_path()
filename = input("Please enter the file you would like to create: ")
completepath = path+filename
create_file()
show_file()
