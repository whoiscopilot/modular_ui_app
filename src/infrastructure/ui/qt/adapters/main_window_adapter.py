# modular_ui_app/src/infrastructure/ui/qt/adapters/main_window_adapter.py
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QResizeEvent, QCloseEvent

from src.core.application.viewmodels.main_viewmodel import MainViewModel
from src.core.application.ports.inbound.i_add_tab_use_case import IAddTabUseCase
from src.core.application.ports.inbound.i_save_state_use_case import ISaveStateUseCase
from src.core.application.ports.inbound.i_restore_state_use_case import IRestoreStateUseCase
from src.core.application.ports.inbound.i_toggle_panel_use_case import ITogglePanelUseCase
from src.core.application.ports.inbound.i_show_sidebar_use_case import IShowSidebarUseCase
from src.core.application.ports.inbound.i_hide_sidebar_use_case import IHideSidebarUseCase
from src.core.application.ports.inbound.i_remove_tab_use_case import IRemoveTabUseCase
from src.infrastructure.ui.qt.adapters.trigger_bar_adapter import TriggerBarAdapter
from src.infrastructure.ui.qt.adapters.animation_adapter import AnimationAdapter
from src.features.panel4.presentation.panel4_view import Panel4View
from src.infrastructure.ui.qt.adapters.splitter_adapter import create_browser_page

class MainWindowAdapter(QMainWindow):
    def __init__(self, viewmodel: MainViewModel, add_tab_uc: IAddTabUseCase, save_uc: ISaveStateUseCase,
                 restore_uc: IRestoreStateUseCase, toggle_panel_uc: ITogglePanelUseCase,
                 show_sidebar_uc: IShowSidebarUseCase, hide_sidebar_uc: IHideSidebarUseCase, remove_tab_uc: IRemoveTabUseCase):
        super().__init__()
        self.viewmodel = viewmodel
        self.add_tab_uc = add_tab_uc
        self.save_uc = save_uc
        self.restore_uc = restore_uc
        self.toggle_panel_uc = toggle_panel_uc
        self.show_sidebar_uc = show_sidebar_uc
        self.hide_sidebar_uc = hide_sidebar_uc
        self.remove_tab_uc = remove_tab_uc

        self.setWindowTitle(self.viewmodel.window_title)
        self.resize(*self.viewmodel.window_size)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_hlayout = QHBoxLayout(central_widget)
        main_hlayout.setContentsMargins(0, 0, 0, 0)

        self.trigger_bar = TriggerBarAdapter(self._show_sidebar)
        main_hlayout.addWidget(self.trigger_bar)

        content_widget = QWidget()
        main_hlayout.addWidget(content_widget, 1)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)

        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("QTabBar::tab { min-width: 120px; }")
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self._close_tab)
        content_layout.addWidget(self.tab_widget)

        plus_button = QPushButton("+")
        plus_button.setFixedSize(30, 30)
        plus_button.clicked.connect(self._add_new_tab)
        self.tab_widget.setCornerWidget(plus_button, Qt.TopRightCorner)

        self._add_new_tab()

        self.panel4 = Panel4View(self.viewmodel.panel4, self._hide_sidebar, parent=self)
        height = self.centralWidget().height()
        self.panel4.setGeometry(QRect(-200, 0, 200, height))
        self.panel4.show()
        self.animation = AnimationAdapter(self.panel4)

        self._bind()
        self.restore_uc.execute()
        self._restore_tabs()

    def _bind(self):
        self.viewmodel.property_changed.connect(self._update_ui)

    def _update_ui(self, prop: str):
        if prop == "tabs":
            pass

    def _add_new_tab(self):
        new_tab_id = self.add_tab_uc.execute()
        page = create_browser_page(new_tab_id)
        index = self.tab_widget.addTab(page, str(new_tab_id))
        self.tab_widget.setCurrentIndex(index)

    def _restore_tabs(self):
        for tab_vm in self.viewmodel.tabs:
            page = create_browser_page(tab_vm.id)
            self.tab_widget.addTab(page, str(tab_vm.id))

    def _close_tab(self, index: int):
        tab_id = int(self.tab_widget.tabText(index))
        self.remove_tab_uc.execute(tab_id)
        self.tab_widget.removeTab(index)
        if self.tab_widget.count() > 0:
            self.tab_widget.setCurrentIndex(index - 1 if index > 0 else 0)

    def _show_sidebar(self):
        if self.viewmodel.panel4.visible:
            return
        self.show_sidebar_uc.execute()
        height = self.centralWidget().height()
        end_geom = QRect(0, 0, 200, height)
        self.animation.anim.stop()  # Diff: Stop previous to prevent overlap/spam
        self.animation.setStartValue(self.panel4.geometry())
        self.animation.setEndValue(end_geom)
        self.animation.start()
        self.panel4.setGeometry(end_geom)
        self.panel4.raise_()
        self.panel4.update()  # Diff: Force repaint for smoothness
        self.viewmodel.panel4.visible = True

    def _hide_sidebar(self):
        if not self.viewmodel.panel4.visible:
            return
        self.hide_sidebar_uc.execute()
        height = self.centralWidget().height()
        start_geom = QRect(-200, 0, 200, height)
        self.animation.anim.stop()  # Diff: Stop previous
        self.animation.setStartValue(self.panel4.geometry())
        self.animation.setEndValue(start_geom)
        self.animation.start()
        self.panel4.setGeometry(start_geom)
        self.panel4.update()  # Diff: Force repaint
        self.viewmodel.panel4.visible = False

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        height = self.centralWidget().height()
        x = -200 if not self.viewmodel.panel4.visible else 0
        new_geom = QRect(x, 0, 200, height)
        self.viewmodel.panel4.geometry = (x, 0, 200, height)
        self.panel4.setGeometry(new_geom)
        self.panel4.update()  # Diff: Repaint on resize for fluid

    def closeEvent(self, event: QCloseEvent):
        self.save_uc.execute()
        super().closeEvent(event)
