# modular_ui_app/src/features/panel6/presentation/panel6_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from src.features.panel6.application.panel6_viewmodel import Panel6ViewModel

class Panel6View(QWidget):
    def __init__(self, viewmodel: Panel6ViewModel):
        super().__init__()
        self.viewmodel = viewmodel
        label = QLabel(self.viewmodel.content, self)
        label.setStyleSheet(self.viewmodel.style)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.addWidget(label, alignment=Qt.AlignCenter)
        self._bind()

    def _bind(self):
        self.viewmodel.property_changed.connect(self._update_ui)

    def _update_ui(self, prop: str):
        pass
