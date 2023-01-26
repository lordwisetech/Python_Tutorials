from tkinter import *
window = Tk()
##window.geometry("270x200")
window.title("my gui")
icon = PhotoImage(file="code.png")
window.iconphoto(True,icon)
window.config(background="#5cfcff")

label = Label(text="hello boy",
              fg="green",
              bg="black",
              font=("Arial",40,"bold"))
def click():
    global count
    count += 1
    print(count)

botton= Button(window,text="FACEBOOK",
               font=("italic",20,"bold"),
               bg="red",
               command=click,
               activebackground="red",
               activeforeground="black",
               )
botton.pack()

label.pack()
def new():
   win = Tk()
   label = Label(win,text="hello ")
   label.pack()

   win.mainloop()



frame = Button(window,text="go to next window",command=new)
frame.pack(side=BOTTOM)


window.mainloop()