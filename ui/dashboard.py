from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class DashboardTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to QuickTrade Dashboard"))
        self.setLayout(layout)
