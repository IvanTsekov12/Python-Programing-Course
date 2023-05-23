import os

src = "C:\\Users\\ivant\\Desktop\\Python stuff\\moving files\\moving file.txt"
dst = "C:\\Programing\\Python Basic-Advanced\\test files\\moving file.txt"

try:
    if os.path.exists(dst):
        print("There is already file there")
    else:
        os.replace(src, dst)
        print(src + " was moved")
except FileNotFoundError:
    print(src + " was not found")