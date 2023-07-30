import socket
from time import *
import time
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import subprocess
import os
import winsound

def load_os():
    GB = 90
    download = 0
    speed = 3
    percent = StringVar()
    loading = Frame(loading_screen, bg='black', bd=5, relief=GROOVE)
    loading.pack()
    text = Label(loading, text='Loading...', font=(40), bg='black', fg='lightgreen', compound='top')
    text.pack()
    bar = Progressbar(loading, orient=HORIZONTAL, length=300)
    bar.pack(pady=10)

    percent_label = Label(loading, font=20, bg='black', fg='white', textvariable=percent).pack()

    while (download < GB):
        time.sleep(0.05)
        bar['value'] += (speed / GB) * 100
        download += speed
        percent.set(str(int((download / GB) * 100)) + "%")
        loading_screen.update_idletasks()
def Startup():
    OS.deiconify()
    root.withdraw()
    loading_screen.withdraw()
    winsound.Beep(400, 200)
    winsound.Beep(500, 200)
    winsound.Beep(800, 400)
def close():
    OS.withdraw()

def Ok():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("", "Blank not allowed")
    elif (uname == "dpteam" and password == "1234"):
        messagebox.showinfo("", "Access Granted!")
        messagebox.showinfo("", "Welcome to DPOS. \n DPOS is loading now...")
        load_os()
        messagebox.showinfo("", "Click OK to see License Agreement")
        messagebox.showwarning("",
                               "By clicking OK you agree that DPOS will have full access to this PC, Download all files and open applications")
        messagebox.showinfo("", "DPOS is ready to be launched, please click OK to run it")
        Startup()
    else:
        messagebox.showinfo("", "Incorrect Username and Password")

root = Tk()
root.title("Access to DPOS")
root.geometry("300x200+450+200")
root.config(bg='lightgreen')
logo = PhotoImage(file='dp logo.png')
root.iconphoto(True, logo)

global e1
global e2

Label(root, text="Username", bg="white").place(x=10, y=10)
Label(root, text="Password", bg="white").place(x=10, y=40)

# entry
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
Button(root, text="Submit", font=("Arial", 20, 'bold'), command=Ok, height=1, width=6).place(x=100, y=100)

#OS window
OS = Toplevel()
OS.title('DPOS')
OS.config(bg='lightblue')
OS.attributes('-fullscreen', True)
OS.withdraw()

#black screen / with loading
loading_screen = Toplevel()
loading_screen.title('')
loading_screen.config(bg='black')
loading_screen.attributes('-fullscreen', True)

#file manager
file_window = Toplevel()
file_window.title('File Manager')
file_window.config(bg='lightyellow')
file_window.geometry('500x200')
file_window.protocol("WM_DELETE_WINDOW", file_window.withdraw)
file_window.withdraw()
#file manager button that runs file manager:
def file_manager_run():
    file_window.deiconify()
file_manager_icon = PhotoImage(file='file_manager.png')
open_file_manager = Button(OS, text='File Manager', bg='white', image=file_manager_icon, compound='top', bd=5, relief=RIDGE, command=file_manager_run).place(x=600,y=450)
#things on the file manager
folder_icon = PhotoImage(file='folder.png')
#python project folder
def open_python_project_folder():
    opened_python_project_folder.deiconify()
opened_python_project_folder = Toplevel()
opened_python_project_folder.title('Python Projects')
opened_python_project_folder.config(bg='lightyellow')
opened_python_project_folder.geometry('500x200')
opened_python_project_folder.protocol("WM_DELETE_WINDOW", opened_python_project_folder.withdraw)
opened_python_project_folder.withdraw()
      #clock.exe file
def clock_application_run():
    os.startfile('Digital Clock.py')
clock_application_logo = PhotoImage(file='exe.png')
clock_exe = Button(opened_python_project_folder, text='Clock.exe', bg='white', image=clock_application_logo, compound='top', command=clock_application_run).place(x=10,y=10)
python_project_folder = Button(file_window, text='Python Projects', bg='white', image=folder_icon, compound='top', command=open_python_project_folder).place(x=10,y=10)

def drawing_machine_run():
    os.startfile('Drawing Machine.py')
drawing_machine_logo = PhotoImage(file='py.png')
drawing_machine = Button(opened_python_project_folder, text='Drawing Machine.py', bg='white', image=drawing_machine_logo, compound='top', command=drawing_machine_run).place(x=100,y=10)

def whiteboard_run():
    os.startfile('Paint.py')
whiteboard_logo = PhotoImage(file='py.png')
whiteboard = Button(opened_python_project_folder, text='Whiteboard.py', bg='white', image=whiteboard_logo, compound='top', command=whiteboard_run).place(x=230,y=10)

def guess_the_num_run():
    os.startfile('Guess the Number with GUI.py')
guess_the_num_logo = PhotoImage(file='py.png')
guess_the_num = Button(opened_python_project_folder, text='Guess the Number.py', bg='white', image=guess_the_num_logo, compound='top', command=guess_the_num_run).place(x=340,y=10)

# colourchooser:
def colourchooser():
    color = colorchooser.askcolor()
    colorHex = color[1]
    OS.config(bg=colorHex)

#taskbar:
def taskbar_colour():
    global colour
    colour = colorchooser.askcolor()[1]
    taskbar.config(bg=colour)

#taskbar.set(bg=colorHexForTaskbar)
taskbar = Label(OS, bd=5, bg='lightyellow', relief=RIDGE, padx=200, pady=20)
taskbar.place(x=450, y=635)

#taskbar apps:
def open_google():
    subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
google_icon = PhotoImage(file='google.png')
google = Button(OS, command = open_google, image = google_icon).place(x=480,y=642)

def open_cmd():
    os.startfile('C:\\WINDOWS\\system32\\cmd.exe')
cmd = Button(OS, command = open_cmd, text='C:\_', bg='black', fg='white', font=(5)).place(x=630, y = 648)

def open_py():
    os.startfile('C:\\Users\\Default\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit).lnk')
py_icon = PhotoImage(file='python.png')
py = Button(OS, command = open_py, image=py_icon).place(x=780, y = 643)

# Apps on desktop:
def BB_run():
    os.startfile('BubbleBlaster.py')
BB_icon = PhotoImage(file='subedited.png')
BBgame = Button(OS, bg = 'white', bd=5, relief=RIDGE, text = 'Bubble Blaster.py', image=BB_icon, compound='top', command = BB_run).place(x=40,y=250)

def calc_run():
    os.startfile('Calculator.py')
calc_icon1 = PhotoImage(file='calculator.png')
calc_program = Button(OS, bg= 'white', bd=5, relief=RIDGE, text = 'Calculator Program.py', image=calc_icon1 , compound='top', command = calc_run).place(x=1100,y=250)

def TE_run():
    os.startfile('Text Editor.py')
TE_icon = PhotoImage(file='text_editor.png')
TE_program = Button(OS, bg='white', bd=5, relief=RIDGE, text= 'Text Editor.py', image=TE_icon, compound='top', command = TE_run).place(x=1000, y=250)

def TTT_run():
    os.startfile('Tic-Tac-Toe.py')
TTT_icon = PhotoImage(file='tictactoe.png')
TTT_program = Button(OS, bg='white', bd=5, relief=RIDGE, text= 'Tic Tac Toe.py', image=TTT_icon, compound='top', width='85', command = TTT_run).place(x=156, y=250)

def snakeGame():
    os.startfile('Snake game.py')
snakeGame_icon= PhotoImage(file='snake.png')
snakeGame = Button(OS, bg='white', bd=5, relief=RIDGE, text= 'Snake Game.py', image=snakeGame_icon, compound='top', width='85', command = snakeGame).place(x=1137, y=370)

def terminal_run():
    os.startfile('Terminal.py')
terminal_icon= PhotoImage(file='terminal.png')
terminal = Button(OS, bg='white', bd=5, relief=RIDGE, text= 'DP Terminal.py', image=terminal_icon, compound='top', width='85', command = terminal_run).place(x=600,y=240)

# clock
clock = Frame(OS, bg='black', bd=5, relief=RAISED)
clock.pack(padx=200, pady=35)

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)

    OS.after(1000, update)


time_label = Label(clock, font=("Arial", 50), fg="white", bg="black")
time_label.pack()

day_label = Label(clock, font=("Ink Free", 25, "bold"), bg="black", fg='lightgreen')
day_label.pack()

date_label = Label(clock, font=("Ink Free", 30), bg="black", fg='lightgreen')
date_label.pack()

update()

# word package apps
microsoft_logo = PhotoImage(file='microsoft.png')
microsoft_background = Label(OS, bg='lightyellow', width=31, height=8, bd=2, relief=RIDGE)
microsoft_background.place(x=10, y=520)
microsoft_label = Label(OS, image=microsoft_logo)
microsoft_label.place(x=56,y=522)

def word_run():
    os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk')
word_logo = PhotoImage(file='word.png')
word = Button(OS, image=word_logo, command=word_run)
word.place(x=13, y=586)

def powerpoint_run():
    os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk')
powerpoint_logo = PhotoImage(file='powerpoint.png')
powerpoint = Button(OS, image=powerpoint_logo, bg='white', command=powerpoint_run)
powerpoint.place(x=68, y=586)

def excel_run():
    os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk')
excel_logo = PhotoImage(file='excel.png')
excel = Button(OS, image=excel_logo, command=excel_run)
excel.place(x=117, y=586)

def outlook_run():
    os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Outlook.lnk')
outlook_logo = PhotoImage(file='outlook.png')
outlook = Button(OS, image=outlook_logo, command=outlook_run)
outlook.place(x=173, y=586)

# themes:
themes = Toplevel()
themes.title('Themes')
themes.config(bg='white')
themes.configure(width=600, height=400)
themes.resizable(False, False)
themes.protocol("WM_DELETE_WINDOW", themes.withdraw)
themes.withdraw()

wallpaper_title = Label(themes, font=('Stencil', 20), fg='red', bg='white', text='Set Colours:')
wallpaper_title.pack()
button_colourchooser = Button(themes, text='Set Background Colour', bg='black', fg='white', font=(20), command = colourchooser)
button_colourchooser.pack()
button_colour_taskbar = Button(themes, text='Set Taskbar Colour', bg='black', fg='white', font=(20), command = taskbar_colour)
button_colour_taskbar.pack()

def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False


def wifi():
    if test_connection() == True:
        messagebox.showinfo("", "You are connected to the Internet")
    else:
        messagebox.showinfo("", "You are not connected to the Internet", icon='error')


def bluetooth():
    messagebox.showinfo("", "Bluetooth is working without any errors")


def display():
    messagebox.showinfo("", "You are connected to a display")

def close_everything():
    OS.withdraw()
    winsound.Beep(400, 200)
    winsound.Beep(600, 250)
    winsound.Beep(400, 200)
    winsound.Beep(250, 500)

def logout():
    OS.withdraw()
    loading_screen.deiconify()
    root.deiconify()
    e1.delete(0, END)
    e2.delete(0, END)

def minimise():
    OS.iconify()
    winsound.Beep(500, 200)
    winsound.Beep(300, 200)
    winsound.Beep(200, 250)

def theme():
    themes.deiconify()

menubar = Menu(OS)
OS.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
theme_menu = Menu(menubar, tearoff=0)
conmenu = Menu(menubar, tearoff=0)
diskmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='•••', menu=filemenu)
filemenu.add_command(label='Minimise', command=minimise)
filemenu.add_command(label='Logout', command=logout)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=close_everything)

menubar.add_cascade(label='Themes', menu=theme_menu)
theme_menu.add_command(label='Edit', command = theme)

menubar.add_cascade(label='Connectivity', menu=conmenu)
conmenu.add_command(label='WiFi', command=wifi)
conmenu.add_command(label='Bluetooth', command=bluetooth)
conmenu.add_command(label='Display', command=display)

menubar.add_cascade(label='Disk Settings', menu=diskmenu)
diskmenu.add_command(label='Edit Disk')
diskmenu.add_command(label='Format Disk')
diskmenu.add_command(label='Eject Disk')

OS.mainloop()
themes.mainloop()
root.mainloop()
loading_screen.mainloop()
