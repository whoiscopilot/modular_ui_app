# modular_ui_app/src/infrastructure/persistence/qt_settings_adapter.py
from PySide6.QtCore import QSettings, QByteArray

from src.core.domain.aggregates.app_state import AppState
from src.core.domain.entities.layout_config import LayoutConfig
from src.core.domain.entities.tab import Tab
from src.core.domain.repositories.i_state_repository import IStateRepository
from src.core.domain.value_objects.geometry import Geometry
from src.core.domain.value_objects.state import State

class QtSettingsAdapter(IStateRepository):
    def __init__(self):
        self.settings = QSettings("MyCompany", "MyApp")

    def save(self, app_state: AppState) -> None:
        self.settings.setValue("num_tabs", app_state.num_tabs)
        for i, tab in enumerate(app_state.tabs):
            self.settings.beginGroup(f"tab_{i}")
            self.settings.setValue("h_splitter_state", QByteArray(tab.layout_config.h_splitter_state.data))
            self.settings.setValue("v_splitter_state", QByteArray(tab.layout_config.v_splitter_state.data))
            self.settings.setValue("outer_v_splitter_state", QByteArray(tab.layout_config.outer_v_splitter_state.data))
            self.settings.setValue("stacked_index", tab.layout_config.stacked_index)
            self.settings.endGroup()

    def load(self) -> AppState:
        num_tabs = self.settings.value("num_tabs", 1, int)
        tabs = []
        for i in range(num_tabs):
            self.settings.beginGroup(f"tab_{i}")
            h_state = State(self.settings.value("h_splitter_state", QByteArray()).data())
            v_state = State(self.settings.value("v_splitter_state", QByteArray()).data())
            outer_state = State(self.settings.value("outer_v_splitter_state", QByteArray()).data())
            stacked_index = self.settings.value("stacked_index", 0, int)
            config = LayoutConfig(h_state, v_state, outer_state, stacked_index, [])
            tabs.append(Tab(id=i+1, layout_config=config, panels=[]))
            self.settings.endGroup()
        return AppState(
            tabs=tabs,
            sidebar_visible=False,
            sidebar_geometry=Geometry(-200, 0, 200, 600),
            num_tabs=num_tabs
        )
