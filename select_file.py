from PyQt5.QtWidgets import QApplication, QFileDialog

def select_file():
    app = QApplication([])
    # file_path, _ = QFileDialog.getOpenFileName(None, "Select a file")
    file_path = './resources/short-story.pdf'
    return file_path