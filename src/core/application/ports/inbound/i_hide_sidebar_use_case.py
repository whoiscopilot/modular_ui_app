# modular_ui_app/src/core/application/ports/inbound/i_hide_sidebar_use_case.py
from abc import ABC, abstractmethod

class IHideSidebarUseCase(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
