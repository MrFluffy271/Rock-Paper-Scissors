#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
import random

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def values():
    global root
    global rock_button_image
    global scissors_button_image
    global paper_button_image
    global player_score
    global bot_score
    global player_selection
    global bot_selection
    player_selection = ""
    bot_selection = ""
    player_score = 0
    bot_score = 0
    root = Tk()
    paper_button_image = PhotoImage(file="./images/Paper.png")
    rock_button_image = PhotoImage(file="./images/Rock.png")
    scissors_button_image = PhotoImage(file="./images/Scissors.png")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_for_bot():
    global randint
    global bot_selection
    global bot_selection_1
    bot_selection_1 = random.randint(1, 3)
    if bot_selection_1 == 1:
        bot_selection = "Rock"
        bot_selection_button()
    elif bot_selection_1 == 2:
        bot_selection = "Paper"
        bot_selection_button()
    elif bot_selection_1 == 3:
        bot_selection = "Scissors"
        bot_selection_button()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def window():
    root.geometry("275x300")
    root.title("Rock, Paper, Scissors")
    root.config(bg="#e4f8ff")
    root.resizable(0, 0)
    root.iconphoto(False, PhotoImage(file='./images/Icon.png'))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game():
    global bot_selection
    global player_selection
    global result
    global player_score
    global bot_score
    if bot_selection == player_selection:
        result = "Draw!"
    elif bot_selection == "Rock" and player_selection == "Paper":
        result = "Player Win!"
        player_score = player_score + 1
    elif bot_selection == "Rock" and player_selection == "Scissors":
        result = "Bot Win!"
        bot_score = bot_score + 1
    elif bot_selection == "Paper" and player_selection == "Rock":
        result = "Bot Win!"
        bot_score = bot_score + 1
    elif bot_selection == "Paper" and player_selection == "Scissors":
        result = "Player Win"
        player_score = player_score + 1
    elif bot_selection == "Scissors" and player_selection == "Rock":
        result = "Player Win"
        player_score = player_score + 1
    elif bot_selection == "Scissors" and player_selection == "Paper":
        result = "Bot Win!"
        bot_score = bot_score + 1


    print(bot_score, "   |   ", player_score)
    print("------------------------------")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bot_selection_button():

    global bot_rock_image
    global bot_rock_button
    global bot_paper_image
    global bot_paper_button
    global bot_scissors_image
    global bot_scissors_button
    global bot_selection
    if bot_selection == "Rock":
        bot_rock_image = PhotoImage(file="./images/Rock.png")
        bot_rock_button = Button(image=bot_rock_image, bg="#e8ffe4", width=50, height=50).place(x=12, y=80)
    elif bot_selection == "Paper":
        bot_paper_image = PhotoImage(file="./images/Paper.png")
        bot_paper_button = Button(image=bot_paper_image, bg="#e8ffe4", width=50, height=50).place(x=12, y=80)
    elif bot_selection == "Scissors":
        bot_scissors_image = PhotoImage(file="./images/Scissors.png")
        bot_paper_button = Button(image=bot_scissors_image, bg="#e8ffe4", width=50, height=50).place(x=12, y=80)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def rock():
    global player_score_Button
    global bot_score_Button
    global rock_image
    global selection_button
    global player_selection
    global result
    global player_score
    global bot_score
    player_selection = "Rock"
    random_for_bot()
    game()
    Button(text=result, bg="#e8ffe4", height=1, width=16).place(x=75, y=260)
    rock_image = PhotoImage(file="./images/Rock.png")
    selection_button = Button(image=rock_image, bg="#e8ffe4", width=50, height=50).place(x=206, y=80)
    player_score_Button = Button(text=player_score, font="arial 10 bold", bg="#e8ffe4", height=1, width=1).place(x=225, y=275)
    bot_score_Button = Button(text=bot_score, font="arial 10 bold", bg="#e8ffe4", height=1, width=1).place(x=28, y=275)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def scissors():
    global player_score_Button
    global bot_score_Button
    global scissors_image
    global selection_button
    global player_selection
    global result
    global player_score
    global bot_score
    random_for_bot()
    player_selection = "Scissors"
    game()
    Button(text=result, bg="#e8ffe4", height=1, width=16).place(x=75, y=260)
    scissors_image = PhotoImage(file="./images/Scissors.png")
    selection_button = Button(image=scissors_image, bg="#e8ffe4", width=50, height=50).place(x=206, y=80)
    player_score_Button = Button(text=player_score, font="arial 10 bold", bg="#e8ffe4", height=1, width=1).place(x=225, y=275)
    bot_score_Button = Button(text=bot_score, font="arial 10 bold", bg="#e8ffe4", height=1, width=1).place(x=28, y=275)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def paper():
    global player_score_Button
    global bot_score_Button
    global paper_image
    global selection_button
    global player_selection
    global result
    global player_score
    global bot_score
    random_for_bot()
    player_selection = "Paper"
    paper_image = PhotoImage(file="./images/Paper.png")
    game()
    Button(text=result, bg="#e8ffe4", height=1, width=16).place(x=75, y=260)
    selection_button = Button(image=paper_image, bg="#e8ffe4", width=50, height=50).place(x=206, y=80)
    player_score_Button = Button(text=player_score, font="arial 10 bold", bg="#e8ffe4",  height=1, width = 1).place(x=225, y=275)
    bot_score_Button = Button(text=bot_score, font="arial 10 bold", bg="#e8ffe4", height=1, width=1).place(x=28, y=275)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def things():
    global bot_rock_Button
    global bot_paper_Button
    global player_selection_label1
    global player_selection_label2
    global bot_selection_label1
    global bot_selection_label2
    global player_selection
    global bot_selection
    global player_score_Label1
    global player_score_Label2
    global bot_score_Label1
    global bot_score_Label2
    global player_score
    global bot_score
    global player_score_Button
    global bot_score_Button
    global scissors_button_image
    global paper_button_image
    global rock_button_image
    global scissors
    global paper
    global rock
    print("---------Game History---------")
    rock = Button(root, image=rock_button_image, font="arial 10 bold", bg="#ffe6e4", command=rock, width=110).place(x=80, y=10)
    scissors = Button(root, image=scissors_button_image, font="arial 10 bold", bg="#ffe6e4", command=scissors,width=110).place(x=80, y=80)
    paper = Button(root, image=paper_button_image, font="arial 10 bold", bg="#ffe6e4", command=paper,width=110).place(x=80, y=150)
    player_score_Label1 = Label(root, text="Player", font="arial 10 bold", bg="#e8ffe4").place(x=213, y=231)
    player_score_Label2 = Label(root, text="Score:", font="arial 10 bold", bg="#e8ffe4").place(x=213, y=253)
    bot_score_Label1 = Label(root, text="Bot", font="arial 10 bold", bg="#e8ffe4").place(x=25, y=231)
    bot_score_Label2 = Label(root, text="Score:", font="arial 10 bold", bg="#e8ffe4").place(x=15, y=253)
    player_selection_label1 = Label(root, text="Player", font="arial 10 bold", bg="#e8ffe4").place(x=212, y=27)
    player_selection_label2 = Label(root, text="Selection:", font="arial 10 bold", bg="#e8ffe4").place(x=200, y=48)
    bot_selection_label1 = Label(root, text="Bot", font="arial 10 bold", bg="#e8ffe4").place(x=27, y=27)
    bot_selection_label2 = Label(root, text="Selection:", font="arial 10 bold", bg="#e8ffe4").place(x=5, y=48)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

values()
things()
window()
mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
