import tkinter

BACKGROUND_COLOR = "#B1DDC6"


class Flashy_UI:
    def __init__(self, words_to_learn):
        self.words_to_learn = words_to_learn
        self.window = tkinter.Tk()

        # SETTING UP THE WINDOW
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.window.title(string="FLASHY")

        # SETTING UP THE CARD
        self.canvas = tkinter.Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
        front_card = tkinter.PhotoImage(file="images/card_front.png")
        back_card = tkinter.PhotoImage(file="images/card_back.png")
        self.canvas.create_image(400, 263, image=front_card)
        self.language = self.canvas.create_text(400, 150, text="Language",  font=("Arial", 40, "italic"), fill="#000000")
        self.word = self.canvas.create_text(400, 263, text="Some Word", font=("Arial", 60, "bold"), fill="#000000")
        self.canvas.grid(row=0, column=0, columnspan=2)

        # SETTING UP THE BUTTONS
        wrong_button = tkinter.PhotoImage(file="images/wrong.png")
        self.wrong_button = tkinter.Button(image=wrong_button, highlightthickness=0)
        self.wrong_button.grid(row=1, column=0)
        right_button = tkinter.PhotoImage(file="images/right.png")
        self.right_button = tkinter.Button(image=right_button, highlightthickness=0)
        self.right_button.grid(row=1, column=1)

        self.window.mainloop()
