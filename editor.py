from PyQt5.QtWidgets import *
import os

app = QApplication([])

window = QWidget()
window.setWindowTitle("Easy Editor")
window.resize(700,500)

btn_directory = QPushButton("Папка")
btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Відзеркалити")
btn_sharpness = QPushButton("Різкість")
btn_black_white = QPushButton("Ч/Б")

lbl_image = QLabel()
list_files = QListWidget()

col1 = QVBoxLayout()
col2 = QVBoxLayout()
row= QHBoxLayout()
row_btns = QHBoxLayout()

col1.addWidget(btn_directory)
col1.addWidget(list_files)
col2.addWidget(lbl_image, 95)

row_btns.addWidget(btn_left)
row_btns.addWidget(btn_right)
row_btns.addWidget(btn_sharpness)
row_btns.addWidget(btn_flip)
row_btns.addWidget(btn_black_white)

col2.addLayout(row_btns)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

window.setLayout(row)

workdir = ""

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def choose_work_directory():
    global workdir
    workdir =QFileDialog.getExistingDirectory()

def show_filenames_list():
    extensions = [".png", ".jpg", ".jpeg", ".gif", "bmp"]
    choose_work_directory()
    filenames = filter(os.listdir(workdir), extensions)
    list_files.clear()
    for filename in filenames:
        list_files.addItem(filename)

btn_directory.clicked.connect(show_filenames_list)

window.show()
app.exec_()