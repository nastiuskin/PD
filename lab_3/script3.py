import os
import random
import shutil

source_dataset_folder = "D:\\ucioba\\PD\\lab_3\\modified_dataset"
destination_dataset_folder = "D:\\ucioba\\PD\\lab_3\\new_dataset"

if not os.path.exists(destination_dataset_folder):
    os.makedirs(destination_dataset_folder)

file_list = os.listdir(source_dataset_folder)

for file in file_list:
    random_number = random.randint(0, 10000)
    
    source_file_path = os.path.join(source_dataset_folder, file)
    new_file_name = f"{random_number}.jpg"
    destination_file_path = os.path.join(destination_dataset_folder, new_file_name)
    
    shutil.copy(source_file_path, destination_file_path)

print("Датасет скопирован с новыми именами успешно.")
