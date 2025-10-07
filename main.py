# modular_ui_app/src/main.py - Entry point
from PySide6.QtWidgets import QApplication

from src.core.domain.aggregates.app_state import AppState
from src.core.domain.services.layout_service import LayoutService
from src.core.domain.services.panel_service import PanelService
from src.core.application.use_cases.add_tab_use_case import AddTabUseCase
from src.core.application.use_cases.toggle_panel_use_case import TogglePanelUseCase
from src.core.application.use_cases.save_state_use_case import SaveStateUseCase
from src.core.application.use_cases.restore_state_use_case import RestoreStateUseCase
from src.core.application.use_cases.show_sidebar_use_case import ShowSidebarUseCase
from src.core.application.use_cases.hide_sidebar_use_case import HideSidebarUseCase
from src.core.application.use_cases.remove_tab_use_case import RemoveTabUseCase  # Diff: Added for tab close logic
from src.core.application.viewmodels.main_viewmodel import MainViewModel
from src.features.panel4.application.panel4_viewmodel import Panel4ViewModel
from src.infrastructure.persistence.qt_settings_adapter import QtSettingsAdapter
from src.infrastructure.ui.qt.adapters.main_window_adapter import MainWindowAdapter

if __name__ == "__main__":
    # Dependency Injection
    app_state = AppState(tabs=[], sidebar_visible=False, sidebar_geometry=(-200, 0, 200, 600), num_tabs=0)
    layout_service = LayoutService()
    panel_service = PanelService()
    repository = QtSettingsAdapter()

    add_tab_uc = AddTabUseCase(app_state, layout_service)
    toggle_panel_uc = TogglePanelUseCase(app_state, layout_service)
    remove_tab_uc = RemoveTabUseCase(app_state, layout_service)  # Diff: Added for tab removal/reset
    save_uc = SaveStateUseCase(app_state, repository)
    restore_uc = RestoreStateUseCase(app_state, repository)
    show_sidebar_uc = ShowSidebarUseCase(app_state)
    hide_sidebar_uc = HideSidebarUseCase(app_state)

    viewmodel = MainViewModel()
    viewmodel.panel4 = Panel4ViewModel()

    # Add initial tab
    add_tab_uc.execute()

    app = QApplication([])
    window = MainWindowAdapter(viewmodel, add_tab_uc, save_uc, restore_uc, toggle_panel_uc, show_sidebar_uc, hide_sidebar_uc, remove_tab_uc)  # Diff: Pass remove_tab_uc
    window.show()
    app.exec()
