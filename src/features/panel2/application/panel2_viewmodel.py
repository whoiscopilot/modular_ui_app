# modular_ui_app/src/features/panel2/application/panel2_viewmodel.py
from src.core.application.viewmodels.base_viewmodel import BaseViewModel
from src.features.panel2.domain.panel2_entity import Panel2Entity

class Panel2ViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        entity = Panel2Entity()
        self.content = entity.content
        self.style = entity.style
