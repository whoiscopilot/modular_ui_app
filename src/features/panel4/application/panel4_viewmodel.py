#src/features/panel4/application/panel4_viewmodel.py
from src.core.application.viewmodels.base_viewmodel import BaseViewModel
from src.core.application.viewmodels.sidebar_viewmodel import SidebarViewModel as CoreSidebarVM  # Reuse for geometry/visible
from src.features.panel4.domain.panel4_entity import Panel4Entity

class Panel4ViewModel(CoreSidebarVM):  # Inherit shared sidebar state
    def __init__(self):
        super().__init__()
        entity = Panel4Entity()
        self.content = entity.content
        self.style = entity.style
        self.is_overlay = entity.is_overlay  # For layout config
