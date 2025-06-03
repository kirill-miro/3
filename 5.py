import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Хрестики-нулики: Гравець vs Бот")
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('consolas', 40), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_winner():
                messagebox.showinfo("Результат", "Ти переміг!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Результат", "Нічия!")
                self.reset_game()
            else:
                self.bot_move()

    def bot_move(self):
        empty = [i for i, val in enumerate(self.board) if val == ""]
        if empty:
            move = random.choice(empty)
            self.board[move] = "O"
            self.buttons[move].config(text="O")
            if self.check_winner():
                messagebox.showinfo("Результат", "Бот переміг!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Результат", "Нічия!")
                self.reset_game()

    def check_winner(self):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for line in wins:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != "":
                return self.board[line[0]]
        return None

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()