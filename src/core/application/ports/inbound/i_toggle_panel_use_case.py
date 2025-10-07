# modular_ui_app/src/core/application/ports/inbound/i_toggle_panel_use_case.py
from abc import ABC, abstractmethod

class ITogglePanelUseCase(ABC):
    @abstractmethod
    def execute(self, tab_id: int) -> int:  # Returns new stacked index
        pass
