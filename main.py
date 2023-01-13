import os
import shutil

for file in os.listdir('Input_folder/'):
    file_path = f"{'Input_folder'}\{file}"
    with open(file_path, 'r') as f:
        try:
            if f.readline()[0]=='S':
                shutil.copy(file_path,f"{'Output_folder'}\{file}")
                print("File copied successfully.")
        except Exception as e:
            print(f'{file} is incorrect')
            shutil.copy(file_path,f"{'Incorrect_file'}\{file}")

