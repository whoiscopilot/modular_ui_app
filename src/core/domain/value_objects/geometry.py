# modular_ui_app/src/core/domain/value_objects/geometry.py  # Value objects for sizes, positions
from dataclasses import dataclass

@dataclass(frozen=True)
class Geometry:
    x: int
    y: int
    width: int
    height: int
