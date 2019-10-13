import os
import sys
import shutil

# This script will organize the given directory by creating subdirectories for 
# the various file types and relocating existing files 






#### DEFINE FILE TYPR DICTIONARY
file_type{
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
    if os.isdir(sys.argv[1]):
        cur_path = sys.argv[1] + "\\" + sys.argv[1].basename + "_{}"
        for f in os.listdir():
            if file_type.get(f.split(".")[-1]) == None:

            else if os.isdir(s.format(file_type.get(f.split(".")[-1])):

    else:
        print("could not find given directory")
        exit()
else:
    print("usage:")
    print("cleanup.py <path_to_directory>")
