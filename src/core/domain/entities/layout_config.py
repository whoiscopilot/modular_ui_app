# modular_ui_app/src/core/domain/entities/layout_config.py  # Entity for overall layout: splitter sizes, stacked index, etc.
from dataclasses import dataclass
from typing import List

from src.core.domain.value_objects.geometry import Geometry
from src.core.domain.value_objects.state import State

@dataclass
class LayoutConfig:
    h_splitter_state: State
    v_splitter_state: State
    outer_v_splitter_state: State
    stacked_index: int
    geometries: List[Geometry]  # For panel sizes/positions if needed
