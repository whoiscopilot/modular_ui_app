# modular_ui_app/src/core/application/ports/inbound/i_add_tab_use_case.py
from abc import ABC, abstractmethod

class IAddTabUseCase(ABC):
    @abstractmethod
    def execute(self) -> int:  # Returns new tab ID
        pass



git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/whoiscopilot/modular_ui_app.git
