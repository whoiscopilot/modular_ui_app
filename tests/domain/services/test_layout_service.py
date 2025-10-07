#tests/core/domain/services/test_layout_service.py
from src.core.domain.services.layout_service import LayoutService
from src.core.domain.aggregates.app_state import AppState

def test_add_tab_creates_valid_tab():
    app_state = AppState(tabs=[], sidebar_visible=False, sidebar_geometry=None, num_tabs=0)
    service = LayoutService()
    tab = service.add_tab(app_state)
    assert tab.id == 1
    assert len(app_state.tabs) == 1
    assert app_state.num_tabs == 1
    assert tab.layout_config.stacked_index == 0
