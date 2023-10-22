import os
import csv

dataset_folder = "D:\\ucioba\\PD\\lab_2\\dataset"
project_root = "D:\\ucioba\\PD\\lab_3"
class_labels = {
    "leopard": "Leopard",
    "tiger": "Tiger",
}

with open("dataset_annotation.csv", mode="w", newline="", encoding="utf-8") as annotation_file:
    annotation_writer = csv.writer(annotation_file)
    annotation_writer.writerow(["Абсолютный путь", "Относительный путь", "Метка класса"])

    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith(".jpg"): 
                absolute_path = os.path.join(root, file)
                relative_path = os.path.relpath(absolute_path, project_root)
                class_label = os.path.basename(root)
                class_name = class_labels.get(class_label, "Неизвестный класс")
                annotation_writer.writerow([absolute_path, relative_path, class_name])

print("Аннотация создана успешно.")
