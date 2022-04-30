import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3

# create a table

'''
conn = sqlite3.connect('Scoreboard.db')
c = conn.cursor()
c.execute("""CREATE TABLE Scoreboard (Name text, Attempt text, Score text)""")
conn.commit()
conn.close()

'''

# table create done that is why we commented this line.

# creating main window

window = Tk()
window.title("Guess the Number")
window.geometry('600x400')
window.configure(bg="#85C1E9")

# adding icon

photo = PhotoImage(file="Icon-Small-40.png")
window.iconphoto(False, photo)

# adding photo

img = ImageTk.PhotoImage(Image.open("200_d.gif"))
myLabel = Label(image=img)
myLabel.place(x=120, y=5)

attempt_count = 0
my_list = []


# ===================================Game functionalities========================================

def new_game():
    game_window = Tk()
    game_window.title("Guess the Number")
    game_window.geometry('600x400')
    game_window.configure(bg="#85C1E9")

    #  =================================random number generate===================================

    random_lower = random.randint(75, 150)  # 75 150
    random_upper = random.randint(225, 290)  # 225 290
    random_number = random.randint(random_lower, random_upper)
    a = random_lower
    b = random_upper

    #  =================================create label to show message==============================

    st = "Guess a number between [ " + str(a) + " ] and [ " + str(b) + " ]"

    message_board = Label(game_window, text=st, bg="#34495E",
                          fg="yellow", font="Arial 12 bold", width=40, height=6, bd=20)
    message_board.place(x=120, y=15)

    # ============================create label to show attempt count==============================

    total_attempt = "Attempt\n[ " + str(0) + " ]"
    show_attempts = Label(game_window, text=total_attempt, bg="#1C2833",
                          fg="yellow", font="Arial 10 bold", width=10, height=3)
    show_attempts.place(x=17, y=18)

    # ==================================create input box==========================================

    input_display = Entry(game_window, font=('Time New Romans', 12, 'bold'), width=35, borderwidth=10,
                          bg="#D5F5E3", fg="black")
    input_display.place(x=120, y=200)

    # ============================read function for check user input================================

    def read():
        global attempt_count
        attempt_count = attempt_count + 1
        current_number = input_display.get()
        my_list.append(current_number)
        input_display.delete(0, END)
        my_score = (100 - attempt_count) + 1

        if int(current_number) > random_upper or int(current_number) < random_lower:
            msg = "Out of Range!\n\nGuess correct Number in Given Range " + " [ " + str(a) + "," + str(b) + "]"
            message_boards = Label(game_window, text=msg, bg="#ECE8DA",
                                   fg="#E60C0C", font="Arial 12 bold", width=40, height=6, bd=20)
            message_boards.place(x=120, y=15)

        elif int(current_number) == random_number:
            msg = "Congratulation! You Guess Correct Number!\n\nAttempt: " + str(
                attempt_count) + "\n\n" + "Score: " + str(
                my_score)
            message_boards = Label(game_window, text=msg, bg="#2C3E50",
                                   fg="#1CDB10", font="Arial 12 bold", width=40, height=6, bd=20)
            message_boards.place(x=120, y=15)
            nm = "Siam"

            conn = sqlite3.connect('Scoreboard.db')
            c = conn.cursor()
            c.execute("INSERT INTO Scoreboard (Name, Attempt, Score) VALUES (?, ?, ?)",
                      (nm, str(attempt_count), str(my_score)))
            conn.commit()
            conn.close()

        elif int(current_number) < random_number:
            msg = "Sorry, guess again. Too low.\n\nChoose a number between [ " + str(a) + " ] and [ " + str(b) + " ]"
            message_boards = Label(game_window, text=msg, bg="#ECE8DA",
                                   fg="#E60C0C", font="Arial 12 bold", width=40, height=6, bd=20)
            message_boards.place(x=120, y=15)

        elif int(current_number) > random_number:
            msg = "Sorry, guess again. Too high.\n\nChoose a number between [ " + str(a) + " ] and [ " + str(b) + " ]"
            message_boards = Label(game_window, text=msg, bg="#ECE8DA",
                                   fg="#E60C0C", font="Arial 12 bold", width=40, height=6, bd=20)
            message_boards.place(x=120, y=15)

        # =============================displaying current attempt count=================================

        msg2 = "Attempt\n[ " + str(attempt_count) + " ]"
        show_attempt = Label(game_window, text=msg2, bg="#1C2833",
                             fg="yellow", font="Arial 10 bold", width=10, height=3)
        show_attempt.place(x=17, y=18)

    # ======================================game window button===========================================

    enter = Button(game_window, text="      Enter      ", padx=3, pady=5, bg="green", fg="white", borderwidth=5,
                   font=('Arial', 9, 'bold'), activebackground="green", activeforeground="white",
                   command=lambda: read())
    enter.place(x=470, y=197)

    # ====================================================================================================

    def show_hint():
        n = random_number
        sum = 0
        while n != 0:
            sum += n % 10
            n = n // 10

        hint_box = Tk()
        hint_box.title("Hints")
        hint_box.geometry("300x50")
        hint_box.configure(bg="yellow")
        msg = "Hint: Sum of digits of the hidden number is " + str(sum)
        hint_message = Label(hint_box, text=msg, bg="yellow",
                             fg="black", font="Arial 9 bold", width=40, height=3)
        hint_message.place(x=3, y=0)
        hint_box.resizable(False, False)
        hint_box.mainloop()

    hints = Button(game_window, text="Help", padx=20, pady=3, bg="#34495E", fg="white", borderwidth=5,
                   font=('Consoles', 9, 'bold'), activebackground="#34495E", activeforeground="white",
                   command=lambda: show_hint())
    hints.place(x=17, y=95)

    # ====================================================================================================

    def show_moves():
        msg = "Moves: "
        for i in range(0, len(my_list)):
            msg += str(my_list[i]) + " "

        move_box = Tk()
        move_box.title("Moves")
        move_box.geometry("300x50")
        move_box.configure(bg="#58D68D")

        move_message = Label(move_box, text=msg, bg="#58D68D",
                             fg="black", font="Arial 9 bold", width=40, height=3)
        move_message.place(x=3, y=0)
        move_box.resizable(False, False)
        move_box.mainloop()

    moves = Button(game_window, text="Moves", padx=13, pady=3, bg="#34495E", fg="white", borderwidth=5,
                   font=('Consoles', 9, 'bold'), activebackground="#34495E", activeforeground="white",
                   command=lambda: show_moves())
    moves.place(x=17, y=135)

    # ====================================================================================================
    game_window.resizable(False, False)
    game_window.mainloop()


# ==========================================================================================================

# ========================================Scoreboard Window===================================

def show_score_board():
    conn = sqlite3.connect('Scoreboard.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Scoreboard")
    item = c.fetchall()
    conn.commit()
    conn.close()

    score_board_window = Tk()
    my_tree = ttk.Treeview(score_board_window)
    my_tree['columns'] = ("Name", "Attempt", "Score")

    # format our column
    my_tree.column("#0", width=120, minwidth=25)
    my_tree.column("Name", anchor=CENTER, width=120)
    my_tree.column("Attempt", anchor=CENTER, width=120)
    my_tree.column("Score", anchor=CENTER, width=120)

    # Creating Headings

    my_tree.heading("#0", text="Label", anchor=CENTER)
    my_tree.heading("Name", text="Name", anchor=CENTER)
    my_tree.heading("Attempt", text="Attempt", anchor=CENTER)
    my_tree.heading("Score", text="Score", anchor=CENTER)

    # Add Data

    for i in range(len(item)):
        my_tree.insert(parent='', index='end', iid=i, text=str(i + 1), values=(item[i][0], item[i][1], item[i][2]))

    my_tree.pack(pady=20)

    score_board_window.title("Scoreboard")
    score_board_window.geometry("600x400")
    score_board_window.configure(bg="#85C1E9")

    score_board_window.resizable(False, False)
    score_board_window.mainloop()


# =====================================Home window Buttons==============================================

btNewGame = Button(window, text="New Game", padx=30, pady=3, bg="green", fg="white", borderwidth=7,
                   font=('Arial', 8, 'bold'), activebackground="green", activeforeground="white",
                   command=lambda: new_game())
btNewGame.place(x=225, y=250)

btScore = Button(window, text="Scoreboard", padx=27, pady=3, bg="#2C3E50", fg="white", borderwidth=7,
                 font=('Arial', 8, 'bold'), activebackground="#2C3E50", activeforeground="white",
                 command=lambda: show_score_board())
btScore.place(x=225, y=290)

btExit = Button(window, text="Exit", padx=50, pady=3, bg="red", fg="white", borderwidth=7, font=('Arial', 8, 'bold'),
                activebackground="red", activeforeground="white", command=window.quit)
btExit.place(x=225, y=330)

window.resizable(False, False)
window.mainloop()

# ================================================END======================================================
