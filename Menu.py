from tkinter import *
from tkinter import Menu
from PIL import Image, ImageTk

root = Tk()
root.title('Game Hub')
root.configure(background='black')
root.geometry("1080x500")


menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar)
Credit_menu = Menu(menubar)

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

Credit_menu.add_command(
    label='Chandra Prakash Singhi (RA1911033010087)'
)

Credit_menu.add_command(
    label='Aaroh Verma (RA1911033010084)'
)

Credit_menu.add_command(
    label='Satyam Verma (RA1911033010085)'
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)

menubar.add_cascade(
    label="Credits",
    menu=Credit_menu
)

def Caterpillar():
    root.destroy()
    import caterpillar
    
def Turtle():
    root.destroy()
    import turtle

b1=Button(root,text='Turtle Betting Game',height=5 ,width=20,bd=3,fg="black",font=("Arial Bold",10),command=Turtle)
b2=Button(root,text='Caterpillar Game',height=5 ,width=20,bd=3,fg="black",font=("Arial Bold",10),command=Caterpillar)
b1.grid(row=2,column=4,padx=5,pady=5)
b2.grid(row=2,column=2,padx=5,pady=5)

name=Label(root,text='GAME HUB',fg="black",font=("Arial Bold",34))
name.grid(row=1,column=3,padx=5,pady=5)

name=Label(root,text='Caterpillar Game',fg="black",font=("Arial Bold",34))
name.grid(row=3,column=2,padx=5,pady=5)

name=Label(root,text='Turtle Betting Game',fg="black",font=("Arial Bold",34))
name.grid(row=3,column=4,padx=5,pady=5)

image = Image.open("3.png")
photo = ImageTk.PhotoImage(image)

piclabel = Label(image=photo)
piclabel.grid(row=4,column=1,columnspan=4)

root.mainloop()