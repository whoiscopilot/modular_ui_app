# modular_ui_app/src/features/panel2/presentation/panel2_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from src.features.panel2.application.panel2_viewmodel import Panel2ViewModel

class Panel2View(QWidget):
    def __init__(self, viewmodel: Panel2ViewModel):
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
        pass  # Similar to Panel1
