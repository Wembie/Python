import tkinter as tk
import random

class DragonTigerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dragon Tiger Game")
        self.root.geometry("450x650")

        self.balance = tk.IntVar()

        self.balance_frame = tk.Frame(root)
        self.balance_frame.pack()

        self.balance_label = tk.Label(self.balance_frame, text="Enter your balance:")
        self.balance_label.grid(row=0, column=0, sticky="W")

        self.balance_entry = tk.Entry(self.balance_frame, textvariable=self.balance, font=("Helvetica", 14))
        self.balance_entry.grid(row=0, column=1)

        self.current_balance_label = tk.Label(root, text="")
        self.current_balance_label.pack()

        self.card_values = {
            "A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "J": 11, "Q": 12, "K": 13
        }
        self.card_suits = ["hearts", "diamonds", "spades", "clubs"]
        self.card_deck = [f"{value} of {suit}" for value in self.card_values for suit in self.card_suits]
        self.min_bet = 1
        self.max_bet = 10000

        self.dragon_label = tk.Label(root, text="Dragon:")
        self.dragon_label.pack()

        self.dragon_card = tk.Label(root, text="", font=("Helvetica", 14))
        self.dragon_card.pack()

        self.tiger_label = tk.Label(root, text="Tiger:")
        self.tiger_label.pack()

        self.tiger_card = tk.Label(root, text="", font=("Helvetica", 14))
        self.tiger_card.pack()

        self.bet_frame = tk.Frame(root)
        self.bet_frame.pack()

        self.bet_label = tk.Label(self.bet_frame, text="Enter your bet amount:")
        self.bet_label.grid(row=0, column=0, sticky="W")

        self.bet_entry = tk.Entry(self.bet_frame, font=("Helvetica", 14))
        self.bet_entry.grid(row=0, column=1)

        self.bet_on_label = tk.Label(self.bet_frame, text="Bet on:")
        self.bet_on_label.grid(row=1, column=0, sticky="W")
        self.bet_on_var = tk.StringVar()
        self.bet_on_var.set("Dragon")

        self.dragon_radio = tk.Radiobutton(self.bet_frame, text="Dragon", variable=self.bet_on_var, value="Dragon")
        self.dragon_radio.grid(row=1, column=1)

        self.tiger_radio = tk.Radiobutton(self.bet_frame, text="Tiger", variable=self.bet_on_var, value="Tiger")
        self.tiger_radio.grid(row=1, column=2)

        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def get_random_card(self):
        return random.choice(self.card_deck)

    def play_game(self):
        if self.balance.get() < self.min_bet:
            self.result_label.config(text="Insufficient balance. Enter a new balance.")
            return

        if not self.bet_entry.get():
            self.result_label.config(text="Enter a bet amount.")
            return

        if int(self.bet_entry.get()) < self.min_bet or int(self.bet_entry.get()) > self.max_bet:
            self.result_label.config(text=f"Bet amount must be between {self.min_bet} and {self.max_bet}.")
            return

        self.balance.set(self.balance.get() - int(self.bet_entry.get()))
        self.current_balance_label.config(text=f"Current Balance: {self.balance.get()}")

        
        dragon_card = self.get_random_card()
        tiger_card = self.get_random_card()
        dragon_card_image = tk.PhotoImage( file = f"cartas/{dragon_card}.png").subsample(5, 5)
        self.dragon_card.config(image=dragon_card_image)
        self.dragon_card.image = dragon_card_image

        tiger_card_image = tk.PhotoImage(file = f"cartas/{tiger_card}.png").subsample(5, 5)
        self.tiger_card.config(image=tiger_card_image)
        self.tiger_card.image = tiger_card_image

        self.dragon_card.config(text=dragon_card)
        self.tiger_card.config(text=tiger_card)

        dragon_value = self.card_values[dragon_card.split(" ")[0]]
        tiger_value = self.card_values[tiger_card.split(" ")[0]]

        if dragon_value > tiger_value:
            if self.bet_on_var.get() == "Dragon":
                self.result_label.config(text="You win!")
                self.balance.set(self.balance.get() + int(self.bet_entry.get() * 2))
            else:
                self.result_label.config(text="You lose.")
        elif dragon_value < tiger_value:
            if self.bet_on_var.get() == "Tiger":
                self.result_label.config(text="You win!")
                self.balance.set(self.balance.get() + int(self.bet_entry.get() * 2))
            else:
                self.result_label.config(text="You lose.")
        else:
            #self.result_
            pass
        self.bet_on_var = tk.StringVar()
        self.bet_on_dragon_rb = tk.Radiobutton(self.bet_frame, text="Dragon", variable=self.bet_on_var, value="Dragon")
        self.bet_on_dragon_rb.grid(row=1, column=1)
        self.bet_on_tiger_rb = tk.Radiobutton(self.bet_frame, text="Tiger", variable=self.bet_on_var, value="Tiger")
        self.bet_on_tiger_rb.grid(row=1, column=2)

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()
        
root = tk.Tk()
app = DragonTigerGame(root)
root.mainloop()
