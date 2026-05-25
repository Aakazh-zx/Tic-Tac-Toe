from tkinter import *
from tkinter import messagebox

# Initialize
root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

Player = "X"
stop_game = False

# Create empty board
b = [[None for _ in range(3)] for _ in range(3)]

# Handle button click
def clicked(r, c):
    global Player, stop_game

    if b[r][c]['text'] == "" and not stop_game:
        b[r][c]['text'] = Player

        if Player == "X":
            Player = "O"
        else:
            Player = "X"

        check_if_win()

# Check winner
def check_if_win():
    global stop_game

    # Rows & Columns
    for i in range(3):
        if b[i][0]['text'] == b[i][1]['text'] == b[i][2]['text'] != "":
            end_game(b[i][0]['text'])
            return
        if b[0][i]['text'] == b[1][i]['text'] == b[2][i]['text'] != "":
            end_game(b[0][i]['text'])
            return

    # Diagonals
    if b[0][0]['text'] == b[1][1]['text'] == b[2][2]['text'] != "":
        end_game(b[0][0]['text'])
        return

    if b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text'] != "":
        end_game(b[0][2]['text'])
        return

    # Tie
    if all(b[i][j]['text'] != "" for i in range(3) for j in range(3)):
        stop_game = True
        messagebox.showinfo("Tie", "It's a Tie!")

# End game
def end_game(winner):
    global stop_game
    stop_game = True
    messagebox.showinfo("Winner", winner + " Won!")

# Restart game
def restart():
    global Player, stop_game
    Player = "X"
    stop_game = False
    for i in range(3):
        for j in range(3):
            b[i][j]['text'] = ""

# Create buttons
for i in range(3):
    for j in range(3):
        b[i][j] = Button(root, text="", height=2, width=4,
                         font=("Helvetica", 20),
                         command=lambda r=i, c=j: clicked(r, c))
        b[i][j].grid(row=i, column=j)

# Restart button
Button(root, text="Restart", font=("Arial", 12),
       command=restart).grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()