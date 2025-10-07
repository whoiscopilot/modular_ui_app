# modular_ui_app/src/core/application/ports/inbound/i_restore_state_use_case.py
from abc import ABC, abstractmethod

class IRestoreStateUseCase(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
