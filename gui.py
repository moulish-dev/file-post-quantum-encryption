import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class HelloApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label at the top
        self.label = QLabel("Hello", self)
        layout.addWidget(self.label)

        # Encrypt Button
        self.encrypt_button = QPushButton("Encrypt", self)
        layout.addWidget(self.encrypt_button)

        # Decrypt Button
        self.decrypt_button = QPushButton("Decrypt", self)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)
        self.setWindowTitle("PyQt Hello App")
        self.setGeometry(100, 100, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloApp()
    window.show()
    sys.exit(app.exec_())
