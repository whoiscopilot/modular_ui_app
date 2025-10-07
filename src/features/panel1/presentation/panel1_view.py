# modular_ui_app/src/features/panel1/presentation/panel1_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from src.features.panel1.application.panel1_viewmodel import Panel1ViewModel

class Panel1View(QWidget):
    def __init__(self, viewmodel: Panel1ViewModel):
        super().__init__()
        self.viewmodel = viewmodel
        label = QLabel(self.viewmodel.content, self)
        label.setStyleSheet(self.viewmodel.style)
        layout = QVBoxLayout(self)
        layout.addWidget(label, alignment=Qt.AlignCenter)
        self._bind()

    def _bind(self):
        self.viewmodel.property_changed.connect(self._update_ui)

    def _update_ui(self, prop: str):
        if prop == "content":
            # Update label if needed
            pass
