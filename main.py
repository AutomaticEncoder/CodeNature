from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import os
import plyer
def run_prj():
    file = filedialog.askopenfilename(title = 'Run Project')
    os.system(file)
def new_prj():
    text.delete(1.0, END)
    root.title('CodeNature - <untitled>')
def open_help():
    os.system('CodeNaturedocumentation.txt')
def open_prj():
    file = filedialog.askopenfilename(title = 'Open Project', defaultextension = '.py',
                                    filetypes = [('Python (.py)','.py'),
                                                 ('Kivy (.kv)', '.kv'),
                                                 ('C++ (.h)', '.h'),
                                                 ('C (.cpp)', '.cpp'),
                                                 ('Java (.java)', '.java'),
                                                 ('C# (.cs)', '.cs '),
                                                 ('Mojo (.mojo)', '.mojo'),
                                                 ('Rust (.rs)', '.rs'),
                                                 ('html (.html)', '.html'),
                                                 ('PHP (.php)', '.php'),
                                                 ('Text files (.txt)', '.txt'),
                                                 ('Blitz Basic files (.bb)', '.bb'),
                                                 ('CSS (.css)', '.css')])
    text.delete(1.0, END)
    p = open(file)
    r = p.read()
    text.insert(1.0, r, END)
def save_prj():
    file = filedialog.asksaveasfile(title = 'Save Project', defaultextension = '.py',
                                    filetypes = [('Python (.py)','.py'),
                                                 ('Kivy (.kv)', '.kv'),
                                                 ('C++ (.h)', '.h'),
                                                 ('C (.cpp)', '.cpp'),
                                                 ('Java (.java)', '.java'),
                                                 ('C# (.cs)', '.cs '),
                                                 ('Mojo (.mojo)', '.mojo'),
                                                 ('Rust (.rs)', '.rs'),
                                                 ('html (.html)', '.html'),
                                                 ('PHP (.php)', '.php'),
                                                 ('Text files (.txt)', '.txt'),
                                                 ('Blitz Basic files (.bb)', '.bb'),
                                                 ('CSS (.css)', '.css')])
    w = text.get(1.0, END)
    file.write(w)
def comment():
    text.insert(1.0, '#\n')
def about_ide():
    showinfo(title = 'CodeNature About', message = 'CodeNature | (C) Pemsietie | python 3.8.10 | version 0.1')
def size_win():
    t = Tk()
    t.geometry('300x300')
    t.resizable(width = False, height =  False)
    def ok():
        h = e.get()
        root.geometry(h)
    t.title('Size window')
    e = Entry(t, bg = 'black', fg = 'white')
    e.pack()
    p = Button(t, text = 'Ok',
               command = ok,
               width = 14)
    p.pack()
    t.mainloop()
def black():
    text['bg'] = 'black'
def white():
    text['bg'] = 'white'
def black1():
    text['fg'] = 'black'
def white1():
    text['fg'] = 'white'
def blue1():
    text['fg'] = 'blue'
def green1():
    text['fg'] = 'green'
def grey1():
    text['fg'] = 'grey'
def yellow1():
    text['fg'] = 'yellow'
root = Tk()
root.geometry('1293x767')
root.title('CodeNature')
menu = Menu(root)
file = Menu(menu, tearoff = 0)
file.add_command(label = 'New', command = new_prj)
file.add_command(label = 'Open', command = open_prj)
file.add_command(label = 'Save', command = save_prj)
file.add_separator()
file.add_command(label = 'Close', command = root.quit)
file.add_command(label = 'Exit', command = root.quit)
menu.add_cascade(label = 'File', menu = file)
Edit = Menu(menu, tearoff = 0)
Edit.add_command(label = 'Add comment', command = comment)
Background = Menu(Edit, tearoff = 0)
Background.add_command(label = 'black', command = black)
Background.add_command(label = 'white', command = white)
Edit.add_cascade(label = 'Background', menu = Background)
Foreground = Menu(Edit, tearoff = 0)
Foreground.add_command(label = 'black', command = black1)
Foreground.add_command(label = 'white', command = white1)
Foreground.add_command(label = 'blue', command = blue1)
Foreground.add_command(label = 'green', command = green1)
Foreground.add_command(label = 'grey', command = grey1)
Foreground.add_command(label = 'yellow', command = yellow1)
Edit.add_cascade(label = 'Foreground', menu = Foreground)
Edit.add_separator()
Edit.add_command(label = 'Size window', command = size_win)
menu.add_cascade(label = 'Edit', menu = Edit)
Run = Menu(menu, tearoff = 0)
Run.add_command(label = 'Run project', command = run_prj)
menu.add_cascade(label = 'Run', menu = Run)
Help = Menu(menu, tearoff = 0)
Help.add_command(label = 'Open documentation', command = open_help)
Help.add_command(label = 'About', command = about_ide)
menu.add_cascade(label = 'Help', menu = Help)
text = Text(width = 700, height = 400, fg = 'blue')
text.pack()
root.config(menu = menu)
root.mainloop()

