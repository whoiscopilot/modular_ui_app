# modular_ui_app/src/features/sidebar/domain/sidebar_entity.py
from src.core.domain.entities.panel import Panel

class SidebarEntity(Panel):
    def __init__(self):
        super().__init__(id="sidebar", content="4", style="color: white; font-size: 50px;")
