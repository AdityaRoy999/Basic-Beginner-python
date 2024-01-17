import os 
import shutil

path = "Folder"

try:
    #os.remove(path)
    #os.rmdir(path) #remove file from root access
    shutil.rmtree(path)
except FileNotFoundError:
    print("That is not found")
except PermissionError:
    print("you don't have permission")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path+"was deleted")