# modular_ui_app/src/features/panel1/application/panel1_viewmodel.py
from src.core.application.viewmodels.base_viewmodel import BaseViewModel
from src.features.panel1.domain.panel1_entity import Panel1Entity

class Panel1ViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        entity = Panel1Entity()
        self.content = entity.content
        self.style = entity.style
