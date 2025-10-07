# modular_ui_app/src/core/application/viewmodels/base_viewmodel.py  # Base MVVM ViewModel
from PySide6.QtCore import QObject, Signal

class BaseViewModel(QObject):
    property_changed = Signal(str)
