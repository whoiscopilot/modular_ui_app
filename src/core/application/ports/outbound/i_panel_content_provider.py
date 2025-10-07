# modular_ui_app/src/core/application/ports/outbound/i_panel_content_provider.py  # For dynamic panel content if needed
from abc import ABC, abstractmethod

from src.core.domain.entities.panel import Panel

class IPanelContentProvider(ABC):
    @abstractmethod
    def get_content(self, panel_id: str) -> Panel:
        pass
