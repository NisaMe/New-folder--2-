from tkinter import *
window=Tk()
window.title("tkinter window")
window.geometry("400x400")
lbl=Label(text="enter your name")
lbl.place(x=100,y=100)
entry= Entry()
entry.place(x=200,y=100)
btn=Button(window,text="submit", bg="yellow")
btn.place(x=200,y=130)

window.mainloop()