 # import tkinter
# here * means to import everything from tkinter
from tkinter import *
 
#  this creates a basic window 
root=Tk()
# geometry defines the height vs width of the window
root.geometry("500x500")
# minsize makes sure that the size of the window is atleast specified in it not less than that
root.minsize(200,200)
# maxsize makes sure that the size of the window is atmost specified in the function
root.maxsize(1000,1000)
# label is like a container where we can put text or images
sumit=Label(text="Sumit Rawat is a Btech undergrad")
sumit.pack()

root.mainloop()

