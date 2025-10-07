# modular_ui_app/src/features/panel3/application/panel3_viewmodel.py
from src.core.application.viewmodels.base_viewmodel import BaseViewModel
from src.features.panel3.domain.panel3_entity import Panel3Entity

class Panel3ViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        entity = Panel3Entity()
        self.content = entity.content
        self.style = entity.style
        self.scrollable = entity.scrollable
