from PyQt5.QtWidgets import QApplication, QFileDialog

def select_file():
    app = QApplication([])
    # file_path, _ = QFileDialog.getOpenFileName(None, "Select a file")
    file_path = './resources/Brave New World.pdf'
    return file_path