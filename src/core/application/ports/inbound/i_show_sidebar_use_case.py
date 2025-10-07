# modular_ui_app/src/core/application/ports/inbound/i_show_sidebar_use_case.py
from abc import ABC, abstractmethod

class IShowSidebarUseCase(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
