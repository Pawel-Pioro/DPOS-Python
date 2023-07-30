#Guess the number game with GUI

from random import randint
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x400+400+150')
window.title('Guess the Number')
window.config(bg='white')
window.withdraw()

guess=IntVar()
global guesses
guesses = IntVar()

def makeRandomNumber():
    global number
    number = randint(1,50)
    
def add1ToGuesses():
    global guesses
    guesses.set(guesses.get()+1)
   

def check():
    if guess.get() < number:
        checkScoreText.configure(text='My number is larger')
        add1ToGuesses()
    elif guess.get() > number:
        checkScoreText.configure(text='My number is smaller')
        add1ToGuesses()
    elif guess.get() == number:
        add1ToGuesses()
        endGame()
    
gameLabel = Label(window, bg='white', text='Guess the Number', font=40, bd = 5, relief = RIDGE)
gameLabel.pack()
text1GameLabel = Label(window, bg='lightyellow', text='Hello, welcome to Guess the Number.', font=30)
text1GameLabel.pack()
text2GameLabel = Label(window, bg='lightyellow',text='Lets begin. My number is between 1 and 50.', font=20)
text2GameLabel.pack()
text3GameLabel = Label(window, bg='white', text='What is my number?', font=15, bd = 5, relief = SUNKEN)
text3GameLabel.place(x=100, y=130)
entry1 = Entry(window, textvariable=guess, bg='lightyellow', font=15)
entry1.place(x=100, y=175)
checkButton = Button(window, bg='lightyellow', font=15, text='Check', command=check)
checkButton.place(x=326, y = 170)
checkScoreText = Label(window, font=15, bd=5, relief = RAISED)
checkScoreText.place(x=100, y=210)
guessesBox = Label(window, bg='#f2fa07', textvariable=guesses, bd=5, relief=SUNKEN)
guessesBox.place(x=60, y=5)
guessesText = Label(window, bg='#f2fa07', text='Guesses:', bd=5, relief=SUNKEN)
guessesText.place(x=5, y=5)
def endGame():
    correctBox = Label(window, font=20, bg='lightgreen', bd=5, relief = SUNKEN, text='You have guessed my number!')
    correctBox.place(x=60, y= 250)
    if messagebox.askyesnocancel('Play Again?', "Do you want to play again?"):
        correctBox.destroy()
        makeRandomNumber()
        entry1.delete(0, END)
        entry1.insert(0, '0')
        guesses.set(0)
    else:
        exit()
        
def playGame():
    window.deiconify()
        
if messagebox.askyesnocancel("Guess the Number game","Do you want to play Guess the Number?"):
    playGame()
else:
    exit()

makeRandomNumber()

window.mainloop()
