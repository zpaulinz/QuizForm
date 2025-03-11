# Copyright (c) 2025 Paulina Zabielska
# All rights reserved. This code cannot be used, copied, modified, or distributed for commercial purposes without the author's permission.

import sys
from PyQt5.QtWidgets import QApplication
from quiz_form import QuizForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuizForm()
    ex.show()
    sys.exit(app.exec_())