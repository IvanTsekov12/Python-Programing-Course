# copyfile() = копира съдържанието на файл
# copy() = copyfile() + mode за удобрение + дестинацията може да е директория(папка)
# copy2() = copy() + копира метаданни (времето на създаването и модификациите на файл)

import shutil

shutil.copyfile("C:\\Programing\\Python Basic-Advanced\\test files\\copying file.txt", "C:\\Programing\\Python Basic-Advanced\\test files\\copied file.txt") #src(source(източник)), дестинация(dst)

