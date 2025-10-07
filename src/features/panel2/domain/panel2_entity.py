# modular_ui_app/src/features/panel2/domain/panel2_entity.py
from src.core.domain.entities.panel import Panel

class Panel2Entity(Panel):
    def __init__(self):
        super().__init__(id="panel2", content="2", style="font-size: 30px;")
