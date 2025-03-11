# Copyright (c) 2025 Paulina Zabielska
# All rights reserved. This code cannot be used, copied, modified, or distributed for commercial purposes without the author's permission.

import os
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer

class SvgButton(QPushButton):
    def __init__(self, disabled_svg, default_svg, active_svg, parent=None):
        super().__init__(parent)
        
        # Check if files exist
        for svg in [disabled_svg, default_svg, active_svg]:
            if not os.path.exists(svg):
                print(f"Plik SVG {svg} nie został znaleziony.")

        # Icons for different states
        self.disabled_renderer = QSvgRenderer(disabled_svg)  # when the button is disabled
        self.default_renderer = QSvgRenderer(default_svg)  # when the button is enabled
        self.active_renderer = QSvgRenderer(active_svg)  # when the mouse is over the enabled

        # Default set as disabled
        self.is_enabled = False
        self.current_renderer = self.disabled_renderer
        self.setIconSize(QSize(30, 30))  


    # Override setEnabled to control the icon
    def setEnabled(self, enabled):
        super().setEnabled(enabled)
        self.is_enabled = enabled
        self.current_renderer = self.default_renderer if enabled else self.disabled_renderer
        self.update()


    # Change icon to active only if the button is enabled
    def enterEvent(self, event):
        if self.is_enabled:
            self.current_renderer = self.active_renderer
            self.update()
        super().enterEvent(event)


    # Revert to the default icon when the mouse leaves
    def leaveEvent(self, event):
        if self.is_enabled:
            self.current_renderer = self.default_renderer
            self.update()
        super().leaveEvent(event)


    # Render the SVG on the button
    def paintEvent(self, event):
        if hasattr(self, "current_renderer"): 
            painter = QPainter(self)
            self.current_renderer.render(painter)
            painter.end()
