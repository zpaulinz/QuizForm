import os
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer

class SvgButton(QPushButton):
    def __init__(self, svg_file, parent=None):
        super().__init__(parent)
        
        # Load the SVG file
        if not os.path.exists(svg_file):
            print(f"Plik SVG {svg_file} nie został znaleziony.")
            return
        self.renderer = QSvgRenderer(svg_file)  
        self.setIconSize(QSize(10, 10))

    # Render the SVG on the button
    def paintEvent(self, event):
        if hasattr(self, "renderer"): 
            painter = QPainter(self)
            self.renderer.render(painter) 
            painter.end()