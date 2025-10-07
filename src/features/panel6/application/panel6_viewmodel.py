# modular_ui_app/src/features/panel6/application/panel6_viewmodel.py
from src.core.application.viewmodels.base_viewmodel import BaseViewModel
from src.features.panel6.domain.panel6_entity import Panel6Entity

class Panel6ViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        entity = Panel6Entity()
        self.content = entity.content
        self.style = entity.style
