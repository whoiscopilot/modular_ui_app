# modular_ui_app/src/core/application/ports/inbound/i_save_state_use_case.py
from abc import ABC, abstractmethod

class ISaveStateUseCase(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
