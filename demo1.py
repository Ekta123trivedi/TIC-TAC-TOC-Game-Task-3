import tkinter as tk
import math


root = tk.Tk()
root.title("Tic Tac Toe")

board = [""] * 9


player_score = 0
computer_score = 0


status = tk.Label(root, text="Your Turn (X)", font=("Arial", 12))
status.grid(row=3, column=0, columnspan=3)


def check_winner():
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None


def minimax(is_max):
    result = check_winner()
    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                best = max(best, minimax(True))
                board[i] = ""
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = ""
        return best


def computer_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    buttons[move]["text"] = "O"
    check_game_over()


def click(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i]["text"] = "X"
        check_game_over()
        if check_winner() is None:
            computer_move()


def check_game_over():
    global player_score, computer_score
    winner = check_winner()
    if winner:
        if winner == "X":
            status.config(text="You Win!")
            player_score += 1
        elif winner == "O":
            status.config(text="Computer Wins!")
            computer_score += 1
        else:
            status.config(text="Draw Game")
        root.after(1500, reset_game)


def reset_game():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="")
    status.config(text=f"Score - You: {player_score}  Computer: {computer_score}")


buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
