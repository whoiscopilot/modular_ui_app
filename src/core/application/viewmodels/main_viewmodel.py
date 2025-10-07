# modular_ui_app/src/core/application/viewmodels/main_viewmodel.py  # For MainWindow
from typing import List

from src.core.application.viewmodels.base_viewmodel import BaseViewModel
from src.core.application.viewmodels.tab_viewmodel import TabViewModel
from src.core.application.viewmodels.sidebar_viewmodel import SidebarViewModel

class MainViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        self.tabs: List[TabViewModel] = []
        self.sidebar: SidebarViewModel = SidebarViewModel()
        self.window_title: str = "Modular UI Application with Advanced QSplitter"
        self.window_size = (800, 600)
