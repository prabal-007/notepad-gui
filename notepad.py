from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
root=Tk()
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

def cut():
    textarea.event_generate(("<<Cut>>"))
def Copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def exi():
    root.destroy()

root.title('Notepad')
canvas_width = 500
canvas_height = 500
root.geometry(f'{canvas_width}x{canvas_height}')

# Status

statusvar = StringVar()
statusvar.set('Ready')
status = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='w')
status.pack(side=BOTTOM, anchor='w', fill=X)

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

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label='Send feedback', command=file)
m2.add_command(label='About us', command=file)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label='Cut', command=cut)
m3.add_command(label='Copy', command=Copy)
m3.add_command(label='Paste', command=paste)
m3.add_command(label='Delete', command=file)

m4 = Menu(mainmenu, tearoff=0)
m4.add_command(label='Resize', command=file)
m4.add_command(label='Exit', command=exi)

root.config(menu=mainmenu)

mainmenu.add_cascade(label='File', menu=m1)
mainmenu.add_cascade(label='Help', menu=m2)
mainmenu.add_cascade(label='Edit', menu=m3)
mainmenu.add_cascade(label='View', menu=m4)


root.mainloop()