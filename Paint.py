from tkinter import *

current_x, current_y = 0,0
color = 'black'

def locate_xy(event):
    
    global current_x, current_y
    
    current_x, current_y = event.x, event.y

def addLine(event):
    
    global current_x, current_y
    
    canvas.create_line((current_x,current_y,event.x,event.y),fill = color)
    current_x, current_y = event.x, event.y
    
def show_color(new_color):
    
    global color
    
    color = new_color

def new_canvas():
    
    canvas.delete('all')
    display_pallete()
    
window = Tk()

window.title('Paint')
#window.state('zoomed')
window.geometry('700x280')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

menubar = Menu(window)
window.config(menu = menubar)
submenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Canvas', command=new_canvas)

canvas= Canvas(window,background='white') 
canvas.grid(row=0,column=0,sticky='nsew')

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>',addLine)

def display_pallete():
    id = canvas.create_rectangle((10,10,30,30),fill='black')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = canvas.create_rectangle((10,40,30,60),fill='gray')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = canvas.create_rectangle((10,70,30,90),fill='brown4')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = canvas.create_rectangle((10,100,30,120),fill='red')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = canvas.create_rectangle((10,130,30,150),fill='orange')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = canvas.create_rectangle((10,160,30,180),fill='yellow')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = canvas.create_rectangle((10,190,30,210),fill='green')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = canvas.create_rectangle((10,220,30,240),fill='blue')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = canvas.create_rectangle((10,250,30,270),fill='purple')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))
    
display_pallete()

window.mainloop()
