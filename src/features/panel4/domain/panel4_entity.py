#src/features/panel4/domain/panel4_entity.py
from src.core.domain.entities.panel import Panel

class Panel4Entity(Panel):
    def __init__(self):
        super().__init__(id="panel4", content="4", style="color: white; font-size: 50px;", is_overlay=True)
