# modular_ui_app/src/infrastructure/ui/qt/adapters/trigger_bar_adapter.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QEnterEvent

class TriggerBarAdapter(QWidget):
    def __init__(self, show_sidebar_callback):
        super().__init__()
        self.show_sidebar_callback = show_sidebar_callback
        self.setFixedWidth(5)  # Original thin sensor (detection on bounds cross)
        self.setStyleSheet("background-color: #f0f0f0; border-right: 1px solid #ccc;")

    def enterEvent(self, event: QEnterEvent):
        self.show_sidebar_callback()  # Direct call to _show_sidebar
        super().enterEvent(event)
