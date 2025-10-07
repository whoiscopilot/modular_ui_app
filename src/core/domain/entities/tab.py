# modular_ui_app/src/core/domain/entities/tab.py  # Aggregate root: Tab with layout config and panels
from dataclasses import dataclass
from typing import List

from src.core.domain.entities.layout_config import LayoutConfig
from src.core.domain.entities.panel import Panel

@dataclass
class Tab:
    id: int
    layout_config: LayoutConfig
    panels: List[Panel]  # References to panel entities (injected via services)
