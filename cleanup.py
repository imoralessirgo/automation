import os
import sys
import shutil

# This script will organize the given directory by creating subdirectories for 
# the various file types and relocating existing files 






#### DEFINE FILE TYPR DICTIONARY
file_type = {
        "pdf":"PDF",
        "doc":"WORD_DOCS",
        "jpg":"IMG",
        "png":"IMG",
        "pptx":"PPP",
        "xls":"EXCEL",
        "txt":"TEXT",
        "exe":"APP"
        }



if len(sys.argv) > 1:
    print(sys.argv[1])
    if os.path.isdir(str(sys.argv[1])):
    
        cur_path = str(sys.argv[1]) + "/" + os.path.basename(sys.argv[1]) + "_{}"
        if not os.path.isdir(cur_path.format("OTHER")):    
            os.mkdir(cur_path.format("OTHER"))
        for f in os.listdir(sys.argv[1]):
            if file_type.get(f.split(".")[-1]) is None:
                shutil.move(str(sys.argv[1]) + "/" + f,cur_path.format("OTHER"))
            elif os.path.isdir(cur_path.format(file_type.get(f.split(".")[-1]))):
                shutil.move(str(sys.argv[1]) + "/" + f,cur_path.format(file_type.get(f.split(".")[-1])))
            else: 
                os.mkdir(cur_path.format(file_type.get(f.split(".")[-1])))
                shutil.move(str(sys.argv[1]) + "/" + f,cur_path.format(file_type.get(f.split(".")[-1])))
    else:
        print("could not find given directory")
        exit()
else:
    print("usage:")
    print("cleanup.py <path_to_directory>")
