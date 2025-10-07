# modular_ui_app/src/core/application/use_cases/restore_state_use_case.py
from src.core.application.ports.inbound.i_restore_state_use_case import IRestoreStateUseCase
from src.core.domain.aggregates.app_state import AppState
from src.core.domain.repositories.i_state_repository import IStateRepository

class RestoreStateUseCase(IRestoreStateUseCase):
    def __init__(self, app_state: AppState, repository: IStateRepository):
        self.app_state = app_state
        self.repository = repository

    def execute(self) -> None:
        loaded_state = self.repository.load()
        self.app_state.tabs = loaded_state.tabs
        self.app_state.sidebar_visible = loaded_state.sidebar_visible
        self.app_state.sidebar_geometry = loaded_state.sidebar_geometry
        self.app_state.num_tabs = loaded_state.num_tabs
