# modular_ui_app/src/core/application/use_cases/toggle_panel_use_case.py
from src.core.application.ports.inbound.i_toggle_panel_use_case import ITogglePanelUseCase
from src.core.domain.aggregates.app_state import AppState
from src.core.domain.services.layout_service import LayoutService

class TogglePanelUseCase(ITogglePanelUseCase):
    def __init__(self, app_state: AppState, layout_service: LayoutService):
        self.app_state = app_state
        self.layout_service = layout_service

    def execute(self, tab_id: int) -> int:
        for tab in self.app_state.tabs:
            if tab.id == tab_id:
                new_index = 1 if tab.layout_config.stacked_index == 0 else 0
                new_config = LayoutConfig(
                    h_splitter_state=tab.layout_config.h_splitter_state,
                    v_splitter_state=tab.layout_config.v_splitter_state,
                    outer_v_splitter_state=tab.layout_config.outer_v_splitter_state,
                    stacked_index=new_index,
                    geometries=tab.layout_config.geometries
                )
                self.layout_service.update_tab_layout(self.app_state, tab_id, new_config)
                return new_index
        return 0
