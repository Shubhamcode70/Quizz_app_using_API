import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Trivia API GUI")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_lbl = tk.Label(text="Score : 0", fg='white', bg=THEME_COLOR)
        self.score_lbl.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250)
        self.display_q = self.canvas.create_text(150, 125, text="THE QUIZZ", font=('arial', 10, 'italic'), width=280)
        self.canvas.grid(columnspan=2, pady=50)

        crs_png = tk.PhotoImage(file="images/false.png")
        chk_png = tk.PhotoImage(file="images/true.png")

        self.chk_btn = tk.Button(image=chk_png, command=self.true_btn)
        self.chk_btn.grid(column=0, row=2)
        self.cross_btn = tk.Button(image=crs_png, command=self.false_btn)
        self.cross_btn.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions:
            self.score_lbl.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.display_q, text=q_text)
        else:
            self.canvas.itemconfig(self.display_q, text="No More Questions Left")
            self.chk_btn.config(state="disabled")
            self.cross_btn.config(state="disabled")

    def true_btn(self):
        self.feedback(self.quiz.check_answer('True'))

    def false_btn(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self, isright):
        if isright:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, self.next_question)
        pass
