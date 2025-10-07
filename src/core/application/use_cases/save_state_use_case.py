# modular_ui_app/src/core/application/use_cases/save_state_use_case.py
from src.core.application.ports.inbound.i_save_state_use_case import ISaveStateUseCase
from src.core.domain.aggregates.app_state import AppState
from src.core.domain.repositories.i_state_repository import IStateRepository

class SaveStateUseCase(ISaveStateUseCase):
    def __init__(self, app_state: AppState, repository: IStateRepository):
        self.app_state = app_state
        self.repository = repository

    def execute(self) -> None:
        self.repository.save(self.app_state)
