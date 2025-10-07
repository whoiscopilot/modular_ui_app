# modular_ui_app/src/features/panel5/application/panel5_viewmodel.py
from src.core.application.viewmodels.base_viewmodel import BaseViewModel
from src.features.panel5.domain.panel5_entity import Panel5Entity

class Panel5ViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        entity = Panel5Entity()
        self.content = entity.content
        self.style = entity.style
        self.scrollable = entity.scrollable
