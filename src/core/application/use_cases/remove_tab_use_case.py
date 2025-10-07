# modular_ui_app/src/core/application/use_cases/remove_tab_use_case.py  # Implements inbound port
from src.core.application.ports.inbound.i_remove_tab_use_case import IRemoveTabUseCase
from src.core.domain.aggregates.app_state import AppState
from src.core.domain.services.layout_service import LayoutService

class RemoveTabUseCase(IRemoveTabUseCase):
    def __init__(self, app_state: AppState, layout_service: LayoutService):
        self.app_state = app_state
        self.layout_service = layout_service

    def execute(self, tab_id: int) -> None:
        self.app_state.tabs = [tab for tab in self.app_state.tabs if tab.id != tab_id]
        if not self.app_state.tabs:
            self.app_state.num_tabs = 0  # Diff: Reset on empty for next add to start at 1
        else:
            self.app_state.num_tabs = max(tab.id for tab in self.app_state.tabs)  # Update to max active ID
