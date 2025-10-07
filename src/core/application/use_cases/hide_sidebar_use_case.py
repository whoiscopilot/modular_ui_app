# modular_ui_app/src/core/application/use_cases/hide_sidebar_use_case.py
from src.core.application.ports.inbound.i_hide_sidebar_use_case import IHideSidebarUseCase
from src.core.domain.aggregates.app_state import AppState
from src.core.domain.value_objects.geometry import Geometry

class HideSidebarUseCase(IHideSidebarUseCase):
    def __init__(self, app_state: AppState):
        self.app_state = app_state

    def execute(self) -> None:
        self.app_state.sidebar_visible = False
        self.app_state.sidebar_geometry = Geometry(-200, 0, 200, self.app_state.sidebar_geometry.height)
