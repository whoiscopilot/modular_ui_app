# modular_ui_app/src/features/panel5/domain/panel5_entity.py
from src.core.domain.entities.panel import Panel

class Panel5Entity(Panel):
    def __init__(self):
        content = "5\n" + "\n".join([f"Scroll line {i}" for i in range(50)])
        super().__init__(id="panel5", content=content, style="font-size: 40px; color: red;", scrollable=True)
