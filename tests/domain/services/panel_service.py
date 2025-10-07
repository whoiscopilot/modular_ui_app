# modular_ui_app/src/core/domain/services/panel_service.py  # Service for panel content management
from src.core.domain.entities.panel import Panel

class PanelService:
    def create_panel(self, panel_id: str, content: str, style: str = None, scrollable: bool = False) -> Panel:
        return Panel(id=panel_id, content=content, style=style, scrollable=scrollable)
