# modular_ui_app/src/core/domain/value_objects/state.py  # Splitter states as value objects
from dataclasses import dataclass

@dataclass(frozen=True)
class State:
    data: bytes  # Serialized state (e.g., from QSplitter.saveState())
