# modular_ui_app/src/infrastructure/ui/qt/components/custom_splitter.py
from PySide6.QtWidgets import QSplitter, QSplitterHandle, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

class CustomSplitterHandle(QSplitterHandle):
    def __init__(self, orientation, parent):
        super().__init__(orientation, parent)
        self.setContentsMargins(0, 0, 0, 0)
        layout = QHBoxLayout(self) if orientation == Qt.Horizontal else QVBoxLayout(self)
        layout.setContentsMargins(2, 2, 2, 2)
        self.collapse_button = QPushButton("<<")
        self.collapse_button.setFixedSize(20, 20)
        self.collapse_button.clicked.connect(self.toggle_collapse)
        layout.addWidget(self.collapse_button)
        self.setMouseTracking(True)

    def toggle_collapse(self):
        splitter = self.splitter()
        index = splitter.indexOf(self)
        if index > 0:
            prev_index = index - 1
            sizes = splitter.sizes()
            is_collapsed = sizes[prev_index] == 0
            splitter.setCollapsible(prev_index, True)
            sizes[prev_index] = 200 if is_collapsed else 0
            splitter.setSizes(sizes)

class CustomSplitter(QSplitter):
    def createHandle(self):
        return CustomSplitterHandle(self.orientation(), self)
