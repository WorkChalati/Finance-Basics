from tkinter import *
from time import strftime
root = Tk()
root.geometry("400x200")
root.resizable(0,0)
root.title('Raed Digital Clock')
Label(root,text = '24 Hour Clock', font ='Biome 20 bold').pack(side=BOTTOM)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('Biome', 40, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()
 
mainloop()
