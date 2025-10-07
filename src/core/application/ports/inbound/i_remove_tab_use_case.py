# modular_ui_app/src/core/application/ports/inbound/i_remove_tab_use_case.py
from abc import ABC, abstractmethod

class IRemoveTabUseCase(ABC):
    @abstractmethod
    def execute(self, tab_id: int) -> None:
        pass
