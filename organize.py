import os
import shutil

from_dir='/Users/pareshgupta/Downloads'
to_dir='/Users/pareshgupta/Desktop/story'

list_of_file=os.listdir(from_dir)
print(list_of_file)

for file_name in list_of_file:
    name, extension=os.path.splitext(file_name)
    
    if extension=='':
        continue
    if extension in ['.png', '.jpg', '.mp3', '.pdf']:
        path1=from_dir+'/'+file_name
        path2=from_dir+'/'+"image_files"
        path3=from_dir+'/'+"image_files"+'/'+file_name

        if os.path.exists(path2):
            print("moving"+file_name+"...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+"...")
            shutil.move(path1, path3)            