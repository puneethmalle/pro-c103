import os
import shutil
import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/sujathakamasani/Desktop"
to_dir = "/Users/sujathakamasani/Desktop/coding/projects/test file"

list_of_files = os.listdir(from_dir)
print(list_of_files)

#Move All the files from downloads folder to Another Folder

class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey,{event.scr_path} has been created")
    def on_deleted(self,event):
        print(f"Opps! someone deleted,{event.scr_path}")
    try:
        while True:
            time.sleep(2)
            print("running...")
    except KeyboardInterrupt:
        print("stopped!")
        Observer.stop()


for file_name in list_of_files:

    name, extension =os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in['.txt', '.pdf','.doc','.docx']:
         

         path1 = from_dir + '/' + file_name
         path2 = from_dir + '/' + "Documents_Files"
         path3 = to_dir + '/' + "Documents_Files" + '/' + file_name



        #shutil.move(from_dir,path2)
    #else:
       # os.mkdir(path2)
        #shutil.move(path,path2)
       # print(path2)
         if os.path.exists(path2): 
          print("Moving"+ file_name + ".....")        

#Move from path1 ---> path3
          shutil.move(path1,path3)
         else:
            os.makedirs(path2)
            print("moving"+file_name+"....")
            shutil.move(path1,path3)