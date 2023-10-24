import os
import shutil
import csv

source_dataset_folder = "D:\\ucioba\\PD\\lab_2\\dataset"

destination_dataset_folder = "D:\\ucioba\\PD\\lab_3\\modified_dataset"

class_labels = {
    "leopard": "Leopard",
    "tiger": "Tiger",
}

if not os.path.exists(destination_dataset_folder):
    os.makedirs(destination_dataset_folder)

with open("dataset_annotation.csv", mode="w", newline="", encoding="utf-8") as annotation_file:
    annotation_writer = csv.writer(annotation_file)
    annotation_writer.writerow(["Абсолютный путь", "Относительный путь", "Метка класса"])

    for root, dirs, files in os.walk(source_dataset_folder):
        for file in files:
            if file.endswith(".jpg"):
                absolute_path = os.path.join(root, file)
                class_label = os.path.basename(root)
                class_name = class_labels.get(class_label, "Неизвестный класс")

                file_name, file_extension = os.path.splitext(file)
                new_file_name = f"{class_label}_{file_name}{file_extension}"

                destination_path = os.path.join(destination_dataset_folder, new_file_name)

                shutil.copy(absolute_path, destination_path)

                relative_path = os.path.relpath(destination_path, os.path.dirname("dataset_annotation.csv"))
                annotation_writer.writerow([destination_path, relative_path, class_name])

print("Датасет скопирован и аннотация создана успешно.")
