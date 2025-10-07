# modular_ui_app/src/features/panel5/presentation/panel5_view.py
from PySide6.QtWidgets import QWidget, QScrollArea, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from src.features.panel5.application.panel5_viewmodel import Panel5ViewModel

class Panel5View(QWidget):
    def __init__(self, viewmodel: Panel5ViewModel):
        super().__init__()
        self.viewmodel = viewmodel
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)
        inner_layout.setContentsMargins(10, 10, 10, 10)
        content_label = QLabel(self.viewmodel.content, inner_widget)
        content_label.setStyleSheet(self.viewmodel.style)
        content_label.setWordWrap(True)
        inner_layout.addWidget(content_label)
        scroll_area.setWidget(inner_widget)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(scroll_area)
        self._bind()

    def _bind(self):
        self.viewmodel.property_changed.connect(self._update_ui)

    def _update_ui(self, prop: str):
        pass
