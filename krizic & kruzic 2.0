from tkinter import*
from pygame import mixer
import pygame
import tkinter

pygame.init()
mixer.init()

pygame.mixer.music.load("D:/2.5/Jan Vlahinić/mixkit-dance-with-me-3.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

turn = "X"
root = Tk()
root.geometry("1150x500")

def buttonFunction1():

    # create the window
    window = tkinter.Tk()
    window.title("Tic Tac Toe")
    window.resizable(0, 0) # Use this secret command to make the window fits all needs, buttons and etc.

    # create 9 buttons and grid them 3x3
    b1 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b1)) # create button
    b1.grid(row=1, column=1) # arrange the buttons in a 3x3 grid

    b2 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b2))
    b2.grid(row=1, column=2)

    b3 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b3))
    b3.grid(row=1, column=3)

    b4 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b4))
    b4.grid(row=2, column=1)

    b5 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b5))
    b5.grid(row=2, column=2)

    b6 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b6))
    b6.grid(row=2, column=3)

    b7 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b7))
    b7.grid(row=3, column=1)

    b8 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b8))
    b8.grid(row=3, column=2)

    b9 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b9))
    b9.grid(row=3, column=3)

    # store buttons in a list
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    # create btn_click function
    def btn_click(btn_clicked):
        btn_clicked['text'] = "X" # change the text of the button
        btn_clicked['state'] = 'disabled' # disable the button
        btn_clicked['bg'] = 'red' # change the background color of the button

        def checkforwinner():
            # if first row is X
            if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if second row is X
            elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if third row is X
            elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if first column is X
            elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if second column is X
            elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if third column is X
            elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if first diagonal is X
            elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if second diagonal is X
            elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            else:
                emptybuttons = []
                if b1['text'] == " ":
                    emptybuttons.append(b1)
                if b2['text'] == " ":
                    emptybuttons.append(b2)
                if b3['text'] == " ":
                    emptybuttons.append(b3)
                if ['text'] == " ":
                    emptybuttons.append(b4)
                if b5 == " ":
                    emptybuttons.append(b5)
                if b6['text'] == " ":
                    emptybuttons.append(b6)
                if b7['text'] == " ":
                    emptybuttons.append(b7)
                if b8['text'] == " ":
                    emptybuttons.append(b8)
                if b9['text'] == " ":
                    emptybuttons.append(b9)

                # randomly select a button from the list
                import random
                random_button = random.choice(emptybuttons)

                # change button text to O
                random_button.config(text="O")

                # make button disabled
                random_button.config(state=tkinter.DISABLED)

                # make O blue
                random_button.config(bg="blue")

                # clear the list
                emptybuttons.clear()

                # if first row is O
                if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

                # if second row is O
                elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

                # if third row is O
                elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

                # if first column is O
                elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

                # if second column is O
                elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

                # if third column is O
                elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

                # if first diagonal is O
                elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

                # if second diagonal is O
                elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
                    # make all buttons disabled
                    for btn in buttons:
                        btn['state'] = 'disabled'
                    tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)
        checkforwinner()

    if __name__ == "__main__":
        window.mainloop()

def buttonFunction2():

    # Create the window
    window = Tk()
    window.title("Tic Tac Toe - PC")
    window.resizable(0, 0) # Use this secret command to make the window fits all needs, buttons and etc.

    # Create the 9 buttons
    button1 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button1))
    button1.grid(row=1, column=1)

    button2 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button2))
    button2.grid(row=1, column=2)

    button3 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button3))
    button3.grid(row=1, column=3)

    button4 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button4))
    button4.grid(row=2, column=1)

    button5 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button5))
    button5.grid(row=2, column=2)

    button6 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button6))
    button6.grid(row=2, column=3)

    button7 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button7))
    button7.grid(row=3, column=1)

    button8 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button8))
    button8.grid(row=3, column=2)

    button9 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button9))
    button9.grid(row=3, column=3)

    # Store buttons in a list
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    # Create turn variable


    # Button_click function
    def button_click(button_clicked):
        global turn
        # We won't need to check if button is empty, because we will make
        # it disabled when we click on it. So it cannot be clicked again.
        if turn == "X":
            # Button text is X and disabled
            button_clicked.config(text="X", state=DISABLED)
            # Button background color
            button_clicked.config(bg="red")
            turn = "O"

        elif turn == "O":
            # We will use elif here not if, or then, it won't work properly
            # Button text is O and disabled
            button_clicked.config(text="O", state=DISABLED)
            # Button background color
            button_clicked.config(bg="blue")
            turn = "X"

        # if first row is X
        if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if first row is O
        elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if second row is X
        elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if second row is O
        elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if third row is X
        elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if third row is O
        elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if first column is X
        elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if first column is O
        elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if second column is X
        elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if second column is O
        elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if third column is X
        elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if third column is O
        elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if first diagonal is X
        elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if first diagonal is O
        elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if second diagonal is X
        elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if second diagonal is O
        elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

        # if all buttons are disabled
        elif button1["state"] == DISABLED and button2["state"] == DISABLED and button3["state"] == DISABLED and button4["state"] == DISABLED and button5["state"] == DISABLED and button6["state"] == DISABLED and button7["state"] == DISABLED and button8["state"] == DISABLED and button9["state"] == DISABLED:
            # Disable all buttons
            for button in buttons:
                button.config(state=DISABLED)
            tkinter.Message(window, text="Draw!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    if __name__ == "__main__":
        window.mainloop()

    
b1 = Button (root, text = "Solo mode", font = ("Times New Roman", 30), command=buttonFunction1, width = 25, height =10, bg = "red")
b1.pack (side=LEFT)

b2 = Button (root, text = "Duo mode", font = ("Times New Roman", 30), command=buttonFunction2, width = 25, height =10, bg = "green")
b2.pack (side=RIGHT)

root.mainloop()
