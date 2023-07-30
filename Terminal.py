from tkinter import*
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

commandCentre = Tk()
commandCentre.configure(bg='black')
commandCentre.geometry('600x300')
commandCentre.title('Terminal')

command = StringVar()

def checkCommand():
    if command.get() == 'ipconfig':
        result.config(text=local_ip)

        

text = Label(commandCentre, bg='black', font=("Arial",20,"bold"), justify='left',fg='lightgreen', text='DPteam DP Corporation \n(C) DPteam Corporation. All rights reserved. \n\nC:/Users/DPteam>')
text.place(x=5, y=5)
entry = Entry(commandCentre, font=("Arial",20,'bold'), bg='black', fg='lightgreen', relief=FLAT, textvariable = command)
entry.place(x=250, y=103)
entry.configure(insertbackground='lightgreen')
entry.focus()
entry.icursor("end")
entry.configure(insertwidth = 5)
submit = Button(commandCentre, text='Submit', bg='black', fg='lightgreen', font=(20), command=checkCommand)
submit.place(x=520, y=100)
result = Label(commandCentre, bg='black', justify='left', fg='lightgreen', font=20)
result.place(x=5, y=150)
    
commandCentre.mainloop()
