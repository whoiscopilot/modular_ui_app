# modular_ui_app/src/core/domain/repositories/i_state_repository.py  # Port/interface for state persistence
from abc import ABC, abstractmethod

from src.core.domain.aggregates.app_state import AppState

class IStateRepository(ABC):
    @abstractmethod
    def save(self, app_state: AppState) -> None:
        pass

    @abstractmethod
    def load(self) -> AppState:
        pass
