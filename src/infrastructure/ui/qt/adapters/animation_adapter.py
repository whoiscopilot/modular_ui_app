# modular_ui_app/src/infrastructure/ui/qt/adapters/animation_adapter.py
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve  # Diff: Added QEasingCurve for smooth animation
from PySide6.QtWidgets import QWidget

class AnimationAdapter:
    def __init__(self, target: QWidget):
        self.target = target
        self.anim = QPropertyAnimation(self.target, b"geometry")
        self.anim.setDuration(150)  # Original fast animation
        self.anim.setEasingCurve(QEasingCurve.OutQuad)  # Diff: Easing for smooth start/end (reduces pixelation/jerk)

    def setStartValue(self, value):
        if isinstance(value, tuple):
            value = QRect(*value)
        self.anim.setStartValue(value)

    def setEndValue(self, value):
        if isinstance(value, tuple):
            value = QRect(*value)
        self.anim.setEndValue(value)

    def start(self):
        self.anim.start()

    def animate_show(self, geometry: tuple):
        height = geometry[3]
        self.setStartValue((-200, 0, 200, height))
        self.setEndValue((0, 0, 200, height))
        self.start()

    def animate_hide(self, geometry: tuple):
        height = geometry[3]
        self.setStartValue((0, 0, 200, height))
        self.setEndValue((-200, 0, 200, height))
        self.start()
