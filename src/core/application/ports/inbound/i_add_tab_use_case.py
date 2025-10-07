# modular_ui_app/src/core/application/ports/inbound/i_add_tab_use_case.py
from abc import ABC, abstractmethod

class IAddTabUseCase(ABC):
    @abstractmethod
    def execute(self) -> int:  # Returns new tab ID
        pass
