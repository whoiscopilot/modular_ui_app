# modular_ui_app/src/core/domain/aggregates/app_state.py  # Root aggregate for entire app: tabs, sidebar, etc.
from dataclasses import dataclass
from typing import List

from src.core.domain.entities.tab import Tab
from src.core.domain.value_objects.geometry import Geometry

@dataclass
class AppState:
    tabs: List[Tab]
    sidebar_visible: bool
    sidebar_geometry: Geometry
    num_tabs: int
