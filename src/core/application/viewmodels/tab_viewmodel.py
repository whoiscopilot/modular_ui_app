# modular_ui_app/src/core/application/viewmodels/tab_viewmodel.py  # Per tab
from src.core.application.viewmodels.base_viewmodel import BaseViewModel

class TabViewModel(BaseViewModel):
    def __init__(self, tab_id: int):
        super().__init__()
        self.id = tab_id
        self.stacked_index: int = 0
        self.switch_button_text: str = "Switch to Panel 5"
