# modular_ui_app/src/features/panel4/presentation/panel4_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QEnterEvent

from src.features.panel4.application.panel4_viewmodel import Panel4ViewModel

class Panel4View(QWidget):
    def __init__(self, viewmodel: Panel4ViewModel, hide_callback, parent=None):  # Diff: Add parent param (default None for flexibility)
        super().__init__(parent)  # Diff: Pass parent to super (child of MainWindow)
        self.viewmodel = viewmodel
        self.hide_callback = hide_callback
        self.setFixedWidth(200)
        inner_widget = QWidget()
        inner_widget.setStyleSheet("background-color: gray;")
        label = QLabel(self.viewmodel.content, inner_widget)
        label.setStyleSheet(self.viewmodel.style)
        layout = QVBoxLayout(inner_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addStretch()
        self_layout = QVBoxLayout(self)
        self_layout.setContentsMargins(0, 0, 0, 0)
        self_layout.addWidget(inner_widget)
        self._bind()

    def _bind(self):
        self.viewmodel.property_changed.connect(self._update_ui)

    def _update_ui(self, prop: str):
        if prop == "visible":
            pass

    def enterEvent(self, event: QEnterEvent):
        super().enterEvent(event)  # No-op: Keeps open

    def leaveEvent(self, event: QEvent):
        self.hide_callback()  # Calls _hide_sidebar
        super().leaveEvent(event)
