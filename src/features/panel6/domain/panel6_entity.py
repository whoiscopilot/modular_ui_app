# modular_ui_app/src/features/panel6/domain/panel6_entity.py
from src.core.domain.entities.panel import Panel

class Panel6Entity(Panel):
    def __init__(self):
        super().__init__(id="panel6", content="6", style="font-size: 24px; font-weight: bold;")
