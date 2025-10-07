# modular_ui_app/src/features/panel1/domain/panel1_entity.py
from src.core.domain.entities.panel import Panel

class Panel1Entity(Panel):
    def __init__(self):
        super().__init__(id="panel1", content="1", style="font-size: 50px;")
