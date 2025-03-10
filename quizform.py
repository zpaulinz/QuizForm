import os
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from svg_button import SvgButton
        
class QuizForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QuizForm")
        self.setFixedSize(600, 600)

        self.load_styles()
        self.layout = QGridLayout(self)
        self.layout.setSpacing(0)
    
        self.layout.setColumnMinimumWidth(0, 20)  # Column1, min width
        self.layout.setColumnMinimumWidth(3, 20)  # Column,  min width


        # Helper functions for creating UI elements
        def create_label(parent, text, object_name, alignment):
            label = QLabel(parent)
            label.setObjectName(object_name)
            label.setAlignment(alignment)
            label.setText(text)
            return label


        def create_input(parent, object_name, placeholder_text=""):
            input_field = QLineEdit(parent)
            input_field.setObjectName(object_name)
            input_field.setAlignment(Qt.AlignCenter)
            input_field.setPlaceholderText(placeholder_text)
            return input_field
        
        
        # Title label setup
        self.title_label = create_label(self, "QuizForm", "titleLabel", Qt.AlignLeft)
        self.layout.addWidget(self.title_label, 0, 0, 1, 4)  # (row, column, row-span, column-span)

        # Header label setup
        self.header_label = create_label(self, "Kreator pytań i odpowiedzi", "headerLabel", Qt.AlignLeft)
        self.layout.addWidget(self.header_label, 1, 0, 1, 4)
        
        # Welcome label setup
        self.welcome_label = create_label(self, "Witaj w Kreatorze pytań i odpowiedzi do aplikacji QuickQuiz!", "welcomeLabel", Qt.AlignCenter)
        self.layout.addWidget(self.welcome_label, 2, 0, 1, 4)
        
        # Info label setup
        self.info_label = create_label(self, "", "infoLabel", Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        self.layout.addWidget(self.info_label, 5, 0, 1, 4)
        
        # Filename label setup
        self.label_filename = create_label(self, "Nazwa pliku (z rozszerzeniem .json):", "filenameLabel", Qt.AlignLeft)
        self.layout.addWidget(self.label_filename, 3, 1, 1, 2)
        
        # Filename input setup
        self.entry_filename = create_input(self, "entryFilenameInput", "")
        self.layout.addWidget(self.entry_filename, 4, 1, 1, 2)

        # Question label setup
        self.label_question = create_label(self, "Treść pytania: (1/1)", "questionLabel", Qt.AlignLeft)       
        self.layout.addWidget(self.label_question, 6, 1, 1, 2)
        
        # Question input setup
        self.entry_question = create_input(self, "entryQuestionInput", "")
        self.layout.addWidget(self.entry_question, 7, 1, 1, 2)
        
        # Correct answer label setup
        self.label_correct_answer = create_label(self, "Poprawna odpowiedź:", "correctAnswerLabel", Qt.AlignLeft)
        self.layout.addWidget(self.label_correct_answer, 8,1,1,2)
        
        # Correct answer input setup
        self.entry_correct_answer = create_input(self, "entryCorrectAnswerInput", "")
        self.layout.addWidget(self.entry_correct_answer, 9,1,1,2)
        
        # Incorrect answer (1) label setup
        self.label_incorrect_answer_1 = create_label(self, "Niepoprawna odpowiedź:", "incorrectAnswerLabel1", Qt.AlignLeft)
        self.layout.addWidget(self.label_incorrect_answer_1, 10, 1, 1, 2)
        
        # Incorrect answer (1) input setup
        self.entry_incorrect_answer_1 = create_input(self, "entryIncorrectAnswerInput1", "")
        self.layout.addWidget(self.entry_incorrect_answer_1, 11, 1, 1, 2)
        
        # Incorrect answer (2) label setup
        self.label_incorrect_answer_2 = create_label(self,'Niepoprawna odpowiedź:', "incorrectAnswerLabel2", Qt.AlignLeft)
        self.layout.addWidget(self.label_incorrect_answer_2, 12,1,1,2)
        
        # Incorrect answer (2) input setup
        self.entry_incorrect_answer_2 = create_input(self, "entryIncorrectAnswerInput2", "")
        self.layout.addWidget(self.entry_incorrect_answer_2, 13,1,1,2)
        
        # Navigation buttons setup
        self.previous_button = SvgButton("img/previous-no.svg", self)
        self.previous_button.setObjectName("previousButton")
        self.layout.addWidget(self.previous_button, 7,0)
        
        self.next_button= SvgButton("img/next-no.svg", self)
        self.next_button.setObjectName("nextButton")
        self.layout.addWidget(self.next_button, 7,3)

        # Save button setup
        self.save_button = SvgButton("img/save-no.svg", self)
        self.save_button.setObjectName("saveButton")
        self.layout.addWidget(self.save_button, 14, 3)
        
        # Footer label setup
        self.footer_label = create_label(self,'', "footerLabel", Qt.AlignCenter)
        self.layout.addWidget(self.footer_label, 15,0,1,4)
    
    
    # Load CSS styles from a file   
    def load_styles(self):
        css_file = 'style.css'
        if os.path.exists(css_file):
            try:
                with open(css_file, 'r') as file:
                    self.setStyleSheet(file.read())
            except Exception as e:
                print(f"Błąd podczas ładowania stylów: {e}")
        else:
            print("Plik style.css nie został znaleziony.")

