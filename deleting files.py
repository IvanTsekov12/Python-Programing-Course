import os, shutil

path = "C:\\Programing\\Python Basic-Advanced\\test files\\deleting dir"

try:
    #os.remove(path) # трие файл
    #os.rmdir(path) # трие празна папка
    shutil.rmtree(path) # трие папка с файлове
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to do that!")
except OSError:
    print("You cannot delete that using that function!")
else:
    print(path + " was deleted")