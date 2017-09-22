from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pyautogui


canvas_width = 300
canvas_height = 300
text2save = []

root = Tk()
currentline = ""
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
        #f.write(text2save) as lines due to text2save being a list
        for item in text2save:
             f.write("%s\n" % item)
        f.close()

def setImage(path):
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(root, image = img)
    panel.image = img
    #events The left mouse button is defined by the event <Button-1>
    panel.bind("<Button-1>", callback)
    panel.grid(column=3, row=1, columnspan = 6, sticky='NS')
#function that is called when clicked Inside the image
def callback(event):
    global currentline
    if(currentline ==""):
        print ("clicked at", event.x, event.y)
        currentline = "name"+str(len(text2save))+","+str(event.x) + ","+str(event.y)+","
    else:
        currentline= currentline +  str(event.x) + ","+str(event.y)
        text2save.append(currentline)
        print(currentline)
        currentline =""
        refreshTextBox()

def delLastRec():
    text2save.pop()
    refreshTextBox()


Button(root, text='Open image', command=openImage).grid(column=1, row =0, sticky='NS', pady=4)
Button(root, text='Delete Last Record', command=delLastRec).grid(column=2, row =0, sticky='NS', pady=4)
Button(root, text='Save', command=saveRec).grid(column=3, row =0, sticky='NS', pady=4)
Button(root, text='Quit', command=onExit).grid(column=4, row =0, sticky='NS', pady=4)
#need a display widget where to show text2save current values, that will update with the selection
displayVar = StringVar(root)#.grid(column=1, row=1, sticky='NS')
displayVar.set("hello, ")
displayVar.set("world")

def refreshTextBox():
    displayVar.set(text2save)
    #add a box drawing for the last selection?
    

mainloop()
