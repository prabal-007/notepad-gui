from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def file():
    pass
def newFile():
    global file
    root.title('Untitled-notepad')
    file=None
    textarea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension='.txt',
    filetype= [('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + '- notepad')
        textarea.delete(1.0, END)
        f = open(file,'r')
        textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile= 'Untitled.txt', defaultextension='.txt',
        filetype= [('All Files', '*.*'), ('Text Documents', '*.txt')])
        if file == "":
            file=None
        else:
            f = open(file,'w')
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + '-Notepad')
    else:
        f = open(file,'w')
        f.write(textarea.get(1.0, END))
        f.close()

def resize():
    def change():
        print(f'{e1.get()}x{e2.get()}')
        root.geometry(f'{e1.get()}x{e2.get()}')
        res.destroy()
    res = Tk()
    Label(res, text='Width').grid()
    # e1 = Entry(res, textvariable=StringVar)
    e1= Scale(res, from_ =100, to = 1530, orient= HORIZONTAL)
    e1.set(canvas_width)
    e1.grid(row=0,column=1)
    Label(res, text='Height').grid(row=1)
    e2= Scale(res, from_ =100, to = 860, orient= HORIZONTAL)
    e2.set(canvas_height)
    e2.grid(row=1, column=1)
    Button(res, text='change', command=change).grid(row=3, column=1)
    res.mainloop

def about():
    abut = Tk()
    abut.title('About us')
    abut.geometry('400x200')
    title= Label(abut,text='About us', font='lucidus 18 bold')
    title.pack(padx='10', pady='10')
    Label(abut,text='''This Notepad ide is developed using Python programming language\nPython Tkinter module is used for gui/user interface\n,
     First commit = 08/07/2020\nMade by Prabal Gupta\ngit- https://github.com/prabal-007/notepad-gui.git''').pack()
    abut.mainloop()

def cut():
    textarea.event_generate(("<<Cut>>"))
def Copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def exi():
    root.destroy()

if __name__ == "__main__":
    root=Tk()
    root.title('Notepad')
    canvas_width = 500
    canvas_height = 500
    root.geometry(f'{canvas_width}x{canvas_height}')

    # Status

    statusvar = StringVar()
    statusvar.set('by Prabal Gupta ')
    status = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='e')
    status.pack(side=BOTTOM, anchor='e', fill=X)

    # Scrollbar & text area
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)

    textarea = Text(root, font='lucida 14', yscrollcommand=scroll.set)
    file = None
    textarea.pack(fill=BOTH, expand=True)
    scroll.config(command=textarea.yview)

    # Menu bar
    mainmenu = Menu(root)
    m1 = Menu(mainmenu, tearoff=0)
    m1.add_command(label='New', command=newFile)
    m1.add_command(label='Open', command=openFile) 
    m1.add_command(label='Save', command=saveFile)
    m1.add_command(label='Save as', command=saveFile)
    m1.add_separator()
    m1.add_command(label='Exit', command=exi)

    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label='Send feedback', command=file)
    m2.add_command(label='About us', command=about)

    m3 = Menu(mainmenu, tearoff=0)
    m3.add_command(label='Cut', command=cut)
    m3.add_command(label='Copy', command=Copy)
    m3.add_command(label='Paste', command=paste)
    m3.add_command(label='Delete', command=file)

    m4 = Menu(mainmenu, tearoff=0)
    m4.add_command(label='Resize', command=resize)
    m4.add_separator()
    m4.add_command(label='Exit', command=exi)

    root.config(menu=mainmenu)

    mainmenu.add_cascade(label='File', menu=m1)
    mainmenu.add_cascade(label='Help', menu=m2)
    mainmenu.add_cascade(label='Edit', menu=m3)
    mainmenu.add_cascade(label='View', menu=m4)

    root.mainloop()
