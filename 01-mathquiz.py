
import tkinter as tk
from tkinter import messagebox
import random


# ------------------------
# Pink Theme Colors
# ------------------------
BG_COLOR = "#FFF0F5"
PINK = "#F45489"
LIGHT_PINK = "#FFB6C1"
DARK_PINK = "#C2185B"
WHITE = "#FFFFFF"
TEXT_COLOR = "#5C3545"
GREEN = "#2E8B57"
RED = "#E53935"


class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Pink Math Quiz")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        self.score = 0
        self.question_count = 0
        self.max_questions = 10
        self.correct_answer = 0
        self.attempt = 1
        self.difficulty = ""

        self.display_menu()

    # ------------------------
    # Clear Screen
    # ------------------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ------------------------
    # Display Menu
    # ------------------------
    def display_menu(self):
        self.clear_screen()

        tk.Label(
            self.root,
            text="♡ MATH QUIZ ♡",
            font=("Arial", 28, "bold"),
            fg=PINK,
            bg=BG_COLOR
        ).pack(pady=30)

        tk.Label(
            self.root,
            text="Choose your difficulty level!",
            font=("Arial", 16),
            fg=TEXT_COLOR,
            bg=BG_COLOR
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="୨୧  DIFFICULTY LEVEL  ୨୧",
            font=("Arial", 18, "bold"),
            fg=DARK_PINK,
            bg=BG_COLOR
        ).pack(pady=20)

        self.create_button("Easy", lambda: self.start_quiz("easy"))
        self.create_button("Moderate", lambda: self.start_quiz("moderate"))
        self.create_button("Advanced", lambda: self.start_quiz("advanced"))

        tk.Label(
            self.root,
            text="Good luck! ♡",
            font=("Arial", 14, "italic"),
            fg=PINK,
            bg=BG_COLOR
        ).pack(pady=25)

    # ------------------------
    # Create Pink Button
    # ------------------------
    def create_button(self, text, command):
        tk.Button(
            self.root,
            text=text,
            font=("Arial", 14, "bold"),
            bg=PINK,
            fg=WHITE,
            activebackground=LIGHT_PINK,
            activeforeground=DARK_PINK,
            width=20,
            relief="flat",
            cursor="hand2",
            command=command
        ).pack(pady=10)

    # ------------------------
    # Start Quiz
    # ------------------------
    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.question_count = 0

        self.clear_screen()

        tk.Label(
            self.root,
            text="♡ MATH QUIZ ♡",
            font=("Arial", 24, "bold"),
            fg=PINK,
            bg=BG_COLOR
        ).pack(pady=20)

        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 24, "bold"),
            fg=DARK_PINK,
            bg=BG_COLOR
        )
        self.question_label.pack(pady=30)

        tk.Label(
            self.root,
            text="Enter your answer below:",
            font=("Arial", 14),
            fg=TEXT_COLOR,
            bg=BG_COLOR
        ).pack(pady=5)

        self.answer_entry = tk.Entry(
            self.root,
            font=("Arial", 18),
            justify="center",
            width=15,
            bg=WHITE,
            fg=DARK_PINK,
            insertbackground=PINK,
            relief="solid",
            bd=2
        )
        self.answer_entry.pack(pady=10)

        tk.Button(
            self.root,
            text="Submit Answer ♡",
            font=("Arial", 13, "bold"),
            bg=PINK,
            fg=WHITE,
            activebackground=LIGHT_PINK,
            width=20,
            relief="flat",
            cursor="hand2",
            command=self.check_answer
        ).pack(pady=10)

        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg=BG_COLOR
        )
        self.feedback_label.pack(pady=10)

        self.progress_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            fg=PINK,
            bg=BG_COLOR
        )
        self.progress_label.pack(pady=10)

        self.score_label = tk.Label(
            self.root,
            text="Score: 0/100",
            font=("Arial", 12, "bold"),
            fg=DARK_PINK,
            bg=BG_COLOR
        )
        self.score_label.pack(pady=5)

        self.answer_entry.bind(
            "<Return>",
            lambda event: self.check_answer()
        )

        self.generate_question()

    # ------------------------
    # Random Integer
    # ------------------------
    def random_int(self):
        if self.difficulty == "easy":
            minimum, maximum = 0, 9

        elif self.difficulty == "moderate":
            minimum, maximum = 10, 99

        else:
            minimum, maximum = 1000, 9999

        return random.randint(minimum, maximum)

    # ------------------------
    # Decide Operation
    # ------------------------
    def decide_operation(self):
        return random.choice(["+", "-"])

    # ------------------------
    # Generate Question
    # ------------------------
    def generate_question(self):
        self.num1 = self.random_int()
        self.num2 = self.random_int()
        self.operation = self.decide_operation()

        if self.operation == "+":
            self.correct_answer = self.num1 + self.num2
        else:
            self.correct_answer = self.num1 - self.num2

        self.attempt = 1
        self.display_problem()

    # ------------------------
    # Display Problem
    # ------------------------
    def display_problem(self):
        self.question_label.config(
            text=f"{self.num1} {self.operation} {self.num2} = ?"
        )

        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

        self.progress_label.config(
            text=f"Question {self.question_count + 1}/{self.max_questions}"
        )

        self.score_label.config(
            text=f"Score: {self.score}/100"
        )

        self.answer_entry.focus()

    # ------------------------
    # Check Correct Answer
    # ------------------------
    def is_correct(self, user_answer):
        return user_answer == self.correct_answer

    # ------------------------
    # Check Answer
    # ------------------------
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number!"
            )
            self.answer_entry.focus()
            return

        if self.is_correct(user_answer):

            if self.attempt == 1:
                self.score += 10
            else:
                self.score += 5

            self.feedback_label.config(
                text="Correct! ♡",
                fg=GREEN
            )

            self.next_question()

        else:
            if self.attempt == 1:
                self.attempt = 2

                self.feedback_label.config(
                    text="Incorrect! Try again!",
                    fg=RED
                )

                self.answer_entry.delete(0, tk.END)
                self.answer_entry.focus()

            else:
                messagebox.showinfo(
                    "Answer",
                    f"Wrong again!\n\n"
                    f"Correct answer: {self.correct_answer}"
                )

                self.next_question()

    # ------------------------
    # Next Question
    # ------------------------
    def next_question(self):
        self.question_count += 1

        if self.question_count == self.max_questions:
            self.display_results()

        else:
            self.generate_question()

    # ------------------------
    # Display Results
    # ------------------------
    def display_results(self):
        self.clear_screen()

        percentage = self.score

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        tk.Label(
            self.root,
            text="♡ QUIZ COMPLETED ♡",
            font=("Arial", 26, "bold"),
            fg=PINK,
            bg=BG_COLOR
        ).pack(pady=35)

        tk.Label(
            self.root,
            text=f"Final Score: {self.score}/100",
            font=("Arial", 22, "bold"),
            fg=DARK_PINK,
            bg=BG_COLOR
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=f"Grade: {grade}",
            font=("Arial", 22, "bold"),
            fg=PINK,
            bg=BG_COLOR
        ).pack(pady=15)

        tk.Label(
            self.root,
            text="Great job for completing the quiz! ♡",
            font=("Arial", 15),
            fg=TEXT_COLOR,
            bg=BG_COLOR
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Play Again ♡",
            font=("Arial", 13, "bold"),
            bg=PINK,
            fg=WHITE,
            activebackground=LIGHT_PINK,
            width=20,
            relief="flat",
            cursor="hand2",
            command=self.display_menu
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Exit",
            font=("Arial", 13, "bold"),
            bg=LIGHT_PINK,
            fg=DARK_PINK,
            activebackground=PINK,
            width=20,
            relief="flat",
            cursor="hand2",
            command=self.root.destroy
        ).pack(pady=10)


# ------------------------
# Run Program
# ------------------------
root = tk.Tk()
quiz = MathQuiz(root)
root.mainloop()
