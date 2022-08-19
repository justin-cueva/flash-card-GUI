from ui import Flashy_UI
from word_data import data

words_to_learn = data.to_dict(orient="records")

# TODO: 1. read the french words csv
# TODO: 2. grap a random word and display it
# TODO: 3. when clicking a button move to a new random card

flashy_ui = Flashy_UI(words_to_learn)
