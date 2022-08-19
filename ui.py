import tkinter
import random
import pandas
import word_data

BACKGROUND_COLOR = "#B1DDC6"


class Flashy_UI:
    def __init__(self, words_to_learn: word_data.data):
        self.words_to_learn = words_to_learn

        self.window = tkinter.Tk()
        self.timer = self.window.after(ms=3000, func=self.flip_card)

        # SETTING UP THE WINDOW
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.window.title(string="FLASHY")

        # SETTING UP THE CARD
        self.canvas = tkinter.Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
        self.front_card = tkinter.PhotoImage(file="images/card_front.png")
        self.back_card = tkinter.PhotoImage(file="images/card_back.png")
        self.current_card_image = self.canvas.create_image(400, 263, image=self.front_card)
        self.language = self.canvas.create_text(400, 150, text="French",  font=("Arial", 40, "italic"), fill="#000000")
        self.word = self.canvas.create_text(400, 263, text="Some Word", font=("Arial", 60, "bold"), fill="#000000")
        self.canvas.grid(row=0, column=0, columnspan=2)

        # SETTING UP THE BUTTONS
        wrong_button = tkinter.PhotoImage(file="images/wrong.png")
        self.wrong_button = tkinter.Button(image=wrong_button, highlightthickness=0, command=self.next_word)
        self.wrong_button.grid(row=1, column=0)
        right_button = tkinter.PhotoImage(file="images/right.png")
        self.right_button = tkinter.Button(image=right_button, highlightthickness=0, command=self.card_is_known)
        self.right_button.grid(row=1, column=1)

        self.next_word()
        self.window.mainloop()

    def next_word(self):
        self.window.after_cancel(self.timer)
        self.current_word = random.choice(self.words_to_learn)
        self.canvas.itemconfig(self.word, text=self.current_word["French"])
        self.canvas.itemconfig(self.current_card_image, image=self.front_card)
        self.canvas.itemconfig(self.language, text="French")
        self.timer = self.window.after(ms=3000, func=self.flip_card)

    def card_is_known(self):
        self.words_to_learn.remove(self.current_word)
        # self.words_to_learn.to_csv("words_to_learn.csv")
        print(len(self.words_to_learn))
        data_frame = pandas.DataFrame(self.words_to_learn)
        data_frame.to_csv("data/words_to_learn.csv", index=False)
        # new_data.to_csv("data/words_to_learn.csv")
        self.next_word()

    def flip_card(self):
        self.canvas.itemconfig(self.word, text=self.current_word["English"])
        self.canvas.itemconfig(self.language, text="English")
        self.canvas.itemconfig(self.current_card_image, image=self.back_card)
