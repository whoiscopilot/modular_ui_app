# modular_ui_app/src/core/application/use_cases/add_tab_use_case.py  # Implements inbound port
from src.core.application.ports.inbound.i_add_tab_use_case import IAddTabUseCase
from src.core.domain.aggregates.app_state import AppState
from src.core.domain.services.layout_service import LayoutService

class AddTabUseCase(IAddTabUseCase):
    def __init__(self, app_state: AppState, layout_service: LayoutService):
        self.app_state = app_state
        self.layout_service = layout_service

    def execute(self) -> int:
        new_tab = self.layout_service.add_tab(self.app_state)
        return new_tab.id
