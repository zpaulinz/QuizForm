# Copyright (c) 2025 Paulina Zabielska
# All rights reserved. This code cannot be used, copied, modified, or distributed for commercial purposes without the author's permission.

import os
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from svg_button import SvgButton
from form_logic import FormLogic
        
class QuizForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QuizForm")
        self.setFixedSize(500, 580)

        self.load_styles()
        self.layout = QGridLayout(self)
        self.layout.setSpacing(0)
    
        self.layout.setColumnMinimumWidth(0, 20)  # Column1, min width
        self.layout.setColumnMinimumWidth(3, 20)  # Column,  min width
        
        self.logic = FormLogic(self)
        
        
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
        self.welcome_label = create_label(self, "", "welcomeLabel", Qt.AlignLeft)
        self.layout.addWidget(self.welcome_label, 2, 0, 1, 4)
        
        # Info label setup
        self.info_label = create_label(self, "", "infoLabel", Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        self.layout.addWidget(self.info_label, 5, 0, 1, 4)
        
        # Filename label setup
        self.label_filename = create_label(self, "Nazwa pliku:", "filenameLabel", Qt.AlignLeft)
        self.layout.addWidget(self.label_filename, 3, 1, 1, 2)
        
        # Filename input setup
        self.entry_filename = create_input(self, "entryFilenameInput", "")
        self.layout.addWidget(self.entry_filename, 4, 1, 1, 2)

        # Question label setup
        self.label_question = create_label(self, "Treść pytania:", "questionLabel", Qt.AlignLeft)       
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
        self.previous_button = SvgButton("img/previous-no.svg", "img/previous.svg", "img/previous-active.svg",self)
        self.previous_button.setObjectName("previousButton")
        self.layout.addWidget(self.previous_button, 7,0)
        
        self.next_button= SvgButton("img/next-no.svg", "img/next.svg", "img/next-active.svg",self)
        self.next_button.setObjectName("nextButton")
        self.layout.addWidget(self.next_button, 7,3)

        # Save button setup
        self.save_button = SvgButton("img/save-no.svg", "img/save.svg", "img/save-active.svg",self)
        self.save_button.setObjectName("saveButton")
        self.layout.addWidget(self.save_button, 14, 3)
        
        # Footer label setup
        self.footer_label = create_label(self,'', "footerLabel", Qt.AlignLeft)
        self.layout.addWidget(self.footer_label, 14,0,1,3)
    
        # Connect to update save button
        self.entry_filename.textChanged.connect(self.logic.update_save_button)
        self.entry_question.textChanged.connect(self.logic.update_save_button)
        self.entry_correct_answer.textChanged.connect(self.logic.update_save_button)
        self.entry_incorrect_answer_1.textChanged.connect(self.logic.update_save_button)
        self.entry_incorrect_answer_2.textChanged.connect(self.logic.update_save_button)
        
        # Connect to update unsaved questions
        self.entry_filename.textChanged.connect(self.logic.update_unsaved_questions)
        self.entry_question.textChanged.connect(self.logic.update_unsaved_questions)
        self.entry_correct_answer.textChanged.connect(self.logic.update_unsaved_questions)
        self.entry_incorrect_answer_1.textChanged.connect(self.logic.update_unsaved_questions)
        self.entry_incorrect_answer_2.textChanged.connect(self.logic.update_unsaved_questions)
        
        ## Connect - save file to json by clicked save button
        self.save_button.clicked.connect(self.logic.save_to_json)

        # Connect to update navigation buttons
        self.entry_filename.textChanged.connect(self.logic.update_navigation_buttons)
        self.entry_question.textChanged.connect(self.logic.update_navigation_buttons)
        self.entry_correct_answer.textChanged.connect(self.logic.update_navigation_buttons)
        self.entry_incorrect_answer_1.textChanged.connect(self.logic.update_navigation_buttons)
        self.entry_incorrect_answer_2.textChanged.connect(self.logic.update_navigation_buttons)
        
        ## Connect Next and previous buttons
        self.next_button.clicked.connect(self.logic.next_button_clicked)
        self.previous_button.clicked.connect(self.logic.previous_button_clicked)

        self.logic.initialize_after_ui_load()
    
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

