from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pyautogui


canvas_width = 300
canvas_height = 300
text2save = "abcd"
root = Tk()
root.geometry("600x400")
root.resizable(width=True, height=True)

def var_states():
   canvas_height = 500
   pyautogui.position()
   print(canvas_height)
   print(canvas_width)

def openImage():
        #Open Callback
        ftypes = [('Image Files', '*.tif *.jpg *.png')]
        dlg = filedialog.Open( filetypes = ftypes)
        filename = dlg.show()
        fn = filename
        #print(fn)
        setImage(fn)

def onExit():
    root.quit()

def saveRec():
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        f.write(text2save)
        f.close()

def setImage(path):
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(root, image = img)
    panel.image = img
    panel.grid(column=3, row=1, columnspan = 6, sticky='NS')



Button(root, text='Open image', command=openImage).grid(column=1, row =0, sticky='NS', pady=4)
Button(root, text='Delete Last Record', command=var_states).grid(column=2, row =0, sticky='NS', pady=4)
Button(root, text='Save', command=saveRec).grid(column=3, row =0, sticky='NS', pady=4)
Button(root, text='Quit', command=onExit).grid(column=4, row =0, sticky='NS', pady=4)
entry = Entry(root).grid(column=1, row=1, sticky='NS')

#events The left mouse button is defined by the event <Button-1>


mainloop()
