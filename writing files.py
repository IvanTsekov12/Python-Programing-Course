text = "This is an appended text" # ако променим текста и with е в writing mode('w'),
#                                                               това ще презапише текста в създаденият файл

with open("C:\\Programing\\Python Basic-Advanced\\test files\\writing files.txt", 'a') as file:
    file.write(text)
