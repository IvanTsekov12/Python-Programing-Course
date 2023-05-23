try:
    with open("C:\\Programing\\Python Basic-Advanced\\test files\\reading file.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!")

