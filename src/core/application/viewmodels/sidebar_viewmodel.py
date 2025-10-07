# modular_ui_app/src/core/application/viewmodels/sidebar_viewmodel.py
from src.core.application.viewmodels.base_viewmodel import BaseViewModel

class SidebarViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        self.visible: bool = False
        self.geometry = ( -200, 0, 200, 600 )  # Initial
