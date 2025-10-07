# modular_ui_app/src/core/domain/entities/panel.py  # Base entity for panels (e.g., content, type)
from dataclasses import dataclass
from typing import Optional

@dataclass
class Panel:
    id: str
    content: str
    style: Optional[str] = None
    scrollable: bool = False
