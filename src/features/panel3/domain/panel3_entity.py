# modular_ui_app/src/features/panel3/domain/panel3_entity.py
from src.core.domain.entities.panel import Panel

class Panel3Entity(Panel):
    def __init__(self):
        content = "3\n" + "\n".join([f"Scroll line {i}" for i in range(50)])
        super().__init__(id="panel3", content=content, style="font-size: 30px; color: green;", scrollable=True)
