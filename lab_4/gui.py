import sys
sys.path.append('lab_3')
sys.path.append('lab_2')

import os
from PySide6 import QtWidgets, QtGui, QtCore
from script1 import create_dataset_annotation
from script4 import create_class_instances_from_directory, get_next_instance
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dataset Annotation Tool')
        self.setGeometry(100, 100, 800, 600)
        
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 0, 0))
        self.setPalette(palette)

        self.label = QtWidgets.QLabel('Select Dataset Folder:')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Arial', 14))

        self.folder_path = QtWidgets.QLineEdit(self)
        self.folder_path.setReadOnly(True)

        self.browse_button = QtWidgets.QPushButton('Browse')
        self.browse_button.clicked.connect(self.browseFolder)

        self.create_annotation_button = QtWidgets.QPushButton('Create Annotation File')
        self.create_annotation_button.clicked.connect(self.createAnnotation)

        self.next_leopard_button = QtWidgets.QPushButton('Next Leopard')
        self.next_leopard_button.clicked.connect(self.getNextInstanceLeopard)

        self.next_tiger_button = QtWidgets.QPushButton('Next Tiger')
        self.next_tiger_button.clicked.connect(self.getNextInstanceTiger)

        self.current_file_path_label = QtWidgets.QLabel(self)
        self.current_file_path_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_file_path_label.setFont(QtGui.QFont('Arial', 12))
        self.current_file_path_label.setStyleSheet("QLabel { background-color : white; }")

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setScaledContents(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.folder_path)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.create_annotation_button)
        layout.addWidget(self.next_leopard_button)
        layout.addWidget(self.next_tiger_button)
        layout.addWidget(self.current_file_path_label)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

        self.dataset_folder = None
        self.project_root = None
        self.class_labels = {
            "leopard": "Leopard",
            "tiger": "Tiger",
        }
        self.annotation_file_path = None
        self.instances = []
        self.used_instances = set()

    def browseFolder(self):
        self.dataset_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.folder_path.setText(self.dataset_folder)
        # Сбросить переменные, связанные с предыдущей папкой
        self.instances = []
        self.used_instances = set()

    def createAnnotation(self):
        if self.dataset_folder:
            if not self.project_root:
                self.project_root = os.path.dirname(self.dataset_folder)

            self.annotation_file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Annotation File', self.project_root, 'CSV Files (*.csv)')

            if self.annotation_file_path:
                create_dataset_annotation(self.dataset_folder, self.project_root, self.class_labels, self.annotation_file_path)

    def getNextInstanceLeopard(self):
        if self.annotation_file_path:
            if not self.instances:
                self.instances = create_class_instances_from_directory(self.dataset_folder)

            next_instance = get_next_instance(self.instances, "leopard", self.used_instances)
            if next_instance:
                self.displayImage(next_instance)
                self.current_file_path_label.setText(f"Current File: {next_instance}")
            else:
                print("No more leopard instances available.")
                self.current_file_path_label.setText("No more files available.")
                self.image_label.clear()  # Очистить QLabel

    def getNextInstanceTiger(self):
        if self.annotation_file_path:
            if not self.instances:
                self.instances = create_class_instances_from_directory(self.dataset_folder)

            next_instance = get_next_instance(self.instances, "tiger", self.used_instances)
            if next_instance:
                self.displayImage(next_instance)
                self.current_file_path_label.setText(f"Current File: {next_instance}")
            else:
                print("No more tiger instances available.")
                self.current_file_path_label.setText("No more files available.")
                self.image_label.clear()  # Очистить QLabel

    def displayImage(self, image_path):
        img = Image.open(image_path)
        img = img.resize((400, 400), Image.ANTIALIAS)
        pixmap = ImageQt(img)
        image = QtGui.QPixmap.fromImage(pixmap)
        self.image_label.setPixmap(image)

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
