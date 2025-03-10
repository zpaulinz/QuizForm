import sys
from PyQt5.QtWidgets import QApplication
from quizform import QuizForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuizForm()
    ex.show()
    sys.exit(app.exec_())