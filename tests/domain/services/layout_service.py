# modular_ui_app/src/core/domain/services/layout_service.py  # Domain service for managing layouts
from src.core.domain.aggregates.app_state import AppState
from src.core.domain.entities.layout_config import LayoutConfig
from src.core.domain.entities.tab import Tab
from src.core.domain.value_objects.state import State  # Added this import

class LayoutService:
    def update_tab_layout(self, app_state: AppState, tab_id: int, new_config: LayoutConfig) -> None:
        for tab in app_state.tabs:
            if tab.id == tab_id:
                tab.layout_config = new_config
                break

    def add_tab(self, app_state: AppState) -> Tab:
        new_tab_id = app_state.num_tabs + 1
        new_tab = Tab(id=new_tab_id, layout_config=LayoutConfig(
            h_splitter_state=State(b''), v_splitter_state=State(b''), outer_v_splitter_state=State(b''),
            stacked_index=0, geometries=[]
        ), panels=[])
        app_state.tabs.append(new_tab)
        app_state.num_tabs = new_tab_id
        return new_tab
