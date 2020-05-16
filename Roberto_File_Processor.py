import os
import json

print("Welcome to my file processor.")

def check_path():
	if os.path.isdir(path):
		print("Great! This directory exists!")
	else:
		print("Sorry, this directory does not exist.")
		exit()

def create_file():
	name = input("What is your name: ")
	address = input("What is your address: ")
	phone_number = input("What is your phone number: ")
	with open(filename, 'w') as filehandle:
		filehandle.write(name+', '+address+', '+phone_number+'\n')
		filehandle.close()

def show_file():
	with open(filename, 'r') as filehandle:
		data = filehandle.read()		
		print(data)

path = input("Please enter a path directory. Mine is /RobertoM91/Python/")
check_path()
if os.path.exists(path):
	filename = input("Please enter the file you would like to create: ")
	create_file()
	show_file()
else:
	print("Sorry, this does not exist")

'''
filename = input("Please enter the file you would like to create: ")
completepath = path+filename
create_file()
print(f"Your file, {filename} has the following data: ")
show_file()
'''