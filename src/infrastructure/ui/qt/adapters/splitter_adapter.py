# modular_ui_app/src/infrastructure/ui/qt/adapters/splitter_adapter.py
from PySide6.QtWidgets import QSplitter, QSplitterHandle, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget
from PySide6.QtCore import Qt

from src.core.application.ports.inbound.i_toggle_panel_use_case import ITogglePanelUseCase
from src.features.panel1.presentation.panel1_view import Panel1View
from src.features.panel1.application.panel1_viewmodel import Panel1ViewModel
from src.features.panel2.presentation.panel2_view import Panel2View
from src.features.panel2.application.panel2_viewmodel import Panel2ViewModel
from src.features.panel3.presentation.panel3_view import Panel3View
from src.features.panel3.application.panel3_viewmodel import Panel3ViewModel
from src.features.panel5.presentation.panel5_view import Panel5View
from src.features.panel5.application.panel5_viewmodel import Panel5ViewModel
from src.features.panel6.presentation.panel6_view import Panel6View
from src.features.panel6.application.panel6_viewmodel import Panel6ViewModel
from src.infrastructure.ui.qt.components.custom_splitter import CustomSplitter

def create_browser_page(tab_id: int, toggle_uc: ITogglePanelUseCase = None):  # Injected if needed
    page = QWidget()
    page_layout = QVBoxLayout(page)
    page_layout.setContentsMargins(0, 0, 0, 0)

    outer_v_splitter = CustomSplitter(Qt.Vertical)
    outer_v_splitter.setOpaqueResize(False)
    page_layout.addWidget(outer_v_splitter)

    h_splitter = CustomSplitter(Qt.Horizontal)
    h_splitter.setOpaqueResize(False)
    outer_v_splitter.addWidget(h_splitter)

    panel1 = Panel1View(Panel1ViewModel())
    h_splitter.addWidget(panel1)

    v_splitter = CustomSplitter(Qt.Vertical)
    v_splitter.setOpaqueResize(False)
    h_splitter.addWidget(v_splitter)

    panel2 = Panel2View(Panel2ViewModel())
    v_splitter.addWidget(panel2)

    switch_container = QWidget()
    switch_container.setFixedHeight(30)
    switch_layout = QHBoxLayout(switch_container)
    switch_layout.setContentsMargins(5, 0, 5, 0)
    switch_btn = QPushButton("Switch to Panel 5")
    switch_btn.setFixedHeight(25)
    switch_layout.addWidget(switch_btn)
    switch_layout.addStretch()
    v_splitter.addWidget(switch_container)
    v_splitter.setCollapsible(1, False)

    stacked_widget = QStackedWidget()
    panel3 = Panel3View(Panel3ViewModel())
    stacked_widget.addWidget(panel3)
    panel5 = Panel5View(Panel5ViewModel())
    stacked_widget.addWidget(panel5)
    v_splitter.addWidget(stacked_widget)

    def toggle_panels():
        new_index = toggle_uc.execute(tab_id) if toggle_uc else (1 if stacked_widget.currentIndex() == 0 else 0)
        stacked_widget.setCurrentIndex(new_index)
        switch_btn.setText("Switch to Panel 3" if new_index == 1 else "Switch to Panel 5")

    switch_btn.clicked.connect(toggle_panels)

    bottom_panel = Panel6View(Panel6ViewModel())
    outer_v_splitter.addWidget(bottom_panel)

    h_splitter.setSizes([500, 300])
    v_splitter.setSizes([150, 30, 120])
    outer_v_splitter.setSizes([98, 2])  # Percentages approximated

    h_splitter.setCollapsible(0, True)
    v_splitter.setChildrenCollapsible(False)
    outer_v_splitter.setCollapsible(1, True)

    # Store for state
    page.h_splitter = h_splitter
    page.v_splitter = v_splitter
    page.outer_v_splitter = outer_v_splitter
    page.stacked_widget = stacked_widget
    page.switch_btn = switch_btn

    return page
