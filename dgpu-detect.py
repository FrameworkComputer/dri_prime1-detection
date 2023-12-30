import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import subprocess

class GPUProcessViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('dGPU-detect')
        self.setGeometry(300, 300, 600, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        self.process_list = QListWidget(self)
        layout.addWidget(self.process_list)

        # Set the font size and make it bold
        self.font = QFont()
        self.font.setPointSize(16)  # Adjust the size as needed
        self.font.setBold(True)

        self.header_font = QFont()
        self.header_font.setPointSize(18)  # Larger font size for the header
        self.header_font.setBold(True)

        self.loadProcesses()

        # Add a close button
        self.close_button = QPushButton('Close', self)
        self.close_button.clicked.connect(self.close)  # Connect the button to the close event
        layout.addWidget(self.close_button)

    def addListItem(self, text, font=None):
        item = QListWidgetItem(text)
        if font:
            item.setFont(font)
        else:
            item.setFont(self.font)
        item.setTextAlignment(Qt.AlignCenter)  # Center align text
        self.process_list.addItem(item)

    def loadProcesses(self):
        cmd = ["ps", "-e", "-o", "pid=", "-o", "comm="]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        gpu_active = False
        for line in proc.stdout:
            pid, comm = line.decode().strip().split(None, 1)
            try:
                with open(f'/proc/{pid}/environ', 'r') as f:
                    environ = f.read()
                    if 'DRI_PRIME' in environ:
                        if not gpu_active:
                            # Add a header indicating that the dGPU is in use
                            self.addListItem("The dGPU is in use by the following processes:", self.header_font)
                            # Add a space after the header
                            self.addListItem("", self.font)
                            gpu_active = True
                        self.addListItem(f"Process '{comm}' (ID {pid}) is using GPU", self.font)
            except Exception:
                pass

        if not gpu_active:
            self.addListItem("No processes are currently using the dGPU.", self.font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GPUProcessViewer()
    ex.show()
    sys.exit(app.exec_())
