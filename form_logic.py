# Copyright (c) 2025 Paulina Zabielska
# All rights reserved. This code cannot be used, copied, modified, or distributed for commercial purposes without the author's permission.

import json
import os

class FormLogic:
    def __init__(self, parent):
        self.parent = parent
        self.questions = [] 
        self.unsaved_questions = []
        
        self.current_question_index = 0 
        self.filename = ""  
        self.max_questions = 100  


    # Check that all fields are completed, including the file name
    def check_all_fields_filled(self):
        filename = self.parent.entry_filename.text().strip()

        if not filename.lower().endswith(".json"):
            filename += ".json"

        filename_filled = filename != ""
        
        question = self.parent.entry_question.text().strip()
        correct_answer = self.parent.entry_correct_answer.text().strip()
        incorrect_answer_1 = self.parent.entry_incorrect_answer_1.text().strip()
        incorrect_answer_2 = self.parent.entry_incorrect_answer_2.text().strip()
        
        all_fields_filled = (question != "" and correct_answer != "" and 
                            incorrect_answer_1 != "" and incorrect_answer_2 != "" 
                            and filename_filled)
        
        print(f"[DEBUG] CHECK FIELDS: question: '{question}', correct: '{correct_answer}', inc1: '{incorrect_answer_1}', inc2: '{incorrect_answer_2}', filename: '{filename}' => {all_fields_filled}")
        return (all_fields_filled)


    # Update save button
    def update_save_button(self):
        all_fields_filled = self.check_all_fields_filled()
        self.parent.save_button.setEnabled(all_fields_filled)
        self.parent.save_button.update()
    
    
    # Update unsaved questions
    def update_unsaved_questions(self):
        all_fields_filled = self.check_all_fields_filled()
        if all_fields_filled:
            question_data = {
                "question": self.parent.entry_question.text().strip(),
                "correct_answer": self.parent.entry_correct_answer.text().strip(),
                "incorrect_answer_1": self.parent.entry_incorrect_answer_1.text().strip(),
                "incorrect_answer_2": self.parent.entry_incorrect_answer_2.text().strip()
            }
            
            # Create question
            question = {
                "question": question_data["question"],
                "options": [
                    question_data["correct_answer"],
                    question_data["incorrect_answer_1"],
                    question_data["incorrect_answer_2"]
                ],
                "correct_answer": question_data["correct_answer"]
            }
        
            # Update the question at the current index or add a new one if it's the first
            if self.unsaved_questions and self.current_question_index < len(self.unsaved_questions):
                self.unsaved_questions[self.current_question_index] = question
            else:
                self.unsaved_questions.append(question)

        print(f"Unsaved questions: {self.unsaved_questions}")
    
    
    # Method called after the form has been fully initialized to safely update the page number
    def initialize_after_ui_load(self):
        self.update_page_number()
    
    
    ## Update and display page number
    def update_page_number(self):
        current_question = self.current_question_index + 1
        self.parent.footer_label.setText(f"Pytanie: {current_question}")
        

    ## Save file to json (or overwrite file)
    def save_to_json(self):
        filename = self.parent.entry_filename.text().strip()
        if not filename.lower().endswith(".json"):
            filename += ".json"

        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(self.unsaved_questions, json_file, indent=4, ensure_ascii=False)
            
            self.parent.footer_label.setText(f"Plik: {filename} został pomyślnie zapisany.")

            ## Add unsaved questions to questions
            for question in self.unsaved_questions:
                self.questions.append(question)

        except Exception as e:
            print(f"Błąd podczas zapisywania pliku JSON: {e}")
            self.parent.footer_label.setText(f"Błąd podczas zapisywania pliku: {e}")
            
        print(f"DEBUG questions: {self.questions}")


    # Update navigation buttons
    def update_navigation_buttons(self):
        all_fields_filled = self.check_all_fields_filled()

        # Block the "Next" button after reached max number of questions
        if len(self.unsaved_questions) >= self.max_questions:
            self.parent.next_button.setEnabled(False)
            self.parent.footer_label.setText(f"Osiągnięto maksymalną liczbę pytań ({self.max_questions}).")
        else:
            self.parent.next_button.setEnabled(all_fields_filled)
            self.parent.next_button.update()

        # Activating the "Previous" button if there is a question
        if len(self.unsaved_questions) > 0 and self.current_question_index > 0:
            self.parent.previous_button.setEnabled(True)
        else:
            self.parent.previous_button.setEnabled(False)


    # Loads a question based on index"""
    def load_question(self, index):
        if index < len(self.unsaved_questions):      
            question = self.unsaved_questions[index]
            self.parent.entry_question.setText(question["question"])
            self.parent.entry_correct_answer.setText(question["correct_answer"])
            self.parent.entry_incorrect_answer_1.setText(question["options"][1])
            self.parent.entry_incorrect_answer_2.setText(question["options"][2])
        else:
            
            self.parent.entry_question.clear()
            self.parent.entry_correct_answer.clear()
            self.parent.entry_incorrect_answer_1.clear()
            self.parent.entry_incorrect_answer_2.clear()
        
            
    # Next button clicked
    def next_button_clicked(self):
        if self.current_question_index < len(self.unsaved_questions):
            self.current_question_index += 1

        self.update_page_number()
        self.load_question(self.current_question_index)


    # Previous button clicked
    def previous_button_clicked(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            
            self.update_page_number()
            self.load_question(self.current_question_index)
