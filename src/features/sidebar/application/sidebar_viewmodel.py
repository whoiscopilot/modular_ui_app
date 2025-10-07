# modular_ui_app/src/features/sidebar/application/sidebar_viewmodel.py
# Note: This is feature-specific, but core has a general one. This extends if needed.
from src.core.application.viewmodels.sidebar_viewmodel import SidebarViewModel as CoreSidebarViewModel
from src.features.sidebar.domain.sidebar_entity import SidebarEntity

class SidebarViewModel(CoreSidebarViewModel):
    def __init__(self):
        super().__init__()
        entity = SidebarEntity()
        self.content = entity.content
        self.style = entity.style
