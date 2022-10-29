from tkinter import *
from datetime import *
class diary:
    def __init__(self,root):
        self.c=Canvas(root)
        self.c.pack(expand=True, fill=BOTH)
        image1=PhotoImage(file="C:\\Users\\Student\\Desktop\\pic.png")
        self.c.img=image1
        self.c.create_image(0, 0, anchor=NW, image=image1)
        self.c.propagate(0)
        self.c.pack()
        self.l3=Label(text='WELCOME TO YOUR PERSONAL DIARY',font=('algerian',38),bg="light pink",fg="black") #Create Label name
        self.l1=Label(text='DIARY USER NAME:',font=('times new roman',24),bg="pink") #Create Label name
        self.l2=Label(text='PASSWORD:',font=('times new roman',24),bg="pink") #Create Label password
        self.e1=Entry(self.c,width=18,fg="black",bg="white", font=('Lucida Calligraphy',24))#Add text entry widget for user name
        self.e2=Entry(self.c,width=18,fg="black",bg="white", font=('times new roman',24),show="*") #Add text entry widget for password
        self.val1=StringVar()
        self.var=IntVar()
        self.b1=Button(self.c,text="LOGIN",font=('times new roman',24),command=self.fnl,bg="pink")#Add Button
        self.b2=Button(self.c,text="REGISTER",font=('times new roman',24),command=self.display,bg="pink")#Add Button
        self.l3.place(x=150,y=80)
        self.l1.place(x=280,y=250)
        self.e1.place(x=600,y=250)
        self.l2.place(x=280,y=350)
        self.e2.place(x=600,y=350)
        self.b1.place(x=300,y=450)
        self.b2.place(x=500,y=450)
        self.c.mainloop()
    def display(self):
        p=Toplevel(root)
        image1=PhotoImage(file="C:\\Users\\Student\\Desktop\\pic.png")
        p.config(background="#2B7878S")
        p.geometry("1550x700+0+0")
        l8=Label(p,image=image1).place(x=0, y=0)
        l9=Label(p,text='REGISTRATION FORM',bg="pink",font=('algerian',38)).place(x=400,y=60)
        l1=Label(p,text='NAME:', bg="pink",font=('times new roman',20)).place(x=350,y=160) 
        l2=Label(p,text='AGE:', bg="pink",font=('times new roman',20)).place(x=350,y=210) 
        l3=Label(p,text='DOB:', bg="pink",font=('times new roman',20)).place(x=350,y=260) 
        l5=Label(p,text='E-MAIL:', bg="pink",font=('times new roman',20)).place(x=350,y=310) 
        l6=Label(p,text='DIARY USER NAME:', bg="pink",font=('times new roman',20)).place(x=350,y=360) 
        l7=Label(p,text='PASSWORD:', bg="pink",font=('times new roman',20)).place(x=350,y=410)
        b1=Button(p,text="REGISTERED",font=('times new roman',15),command=self.fnl,bg="pink",borderwidth=5,relief=RIDGE).place(x=500,y=510)
        e1=Entry(p,width=20,fg="purple",bg="white", font=('Lucida Calligraphy',15)).place(x=700,y=160)
        e2=Entry(p,width=20,fg="purple",bg="white", font=('Lucida Calligraphy',15)).place(x=700,y=210) 
        e3=Entry(p,width=20,fg="purple",bg="white", font=('Lucida Calligraphy',15)).place(x=700,y=260)
        e4=Entry(p,width=20,fg="purple",bg="white", font=('Lucida Calligraphy',15)).place(x=700,y=310)
        e6=Entry(p,width=20,fg="purple",bg="white", font=('Lucida Calligraphy',15)).place(x=700,y=360)
        e7=Entry(p,width=20,fg="purple",bg="white", font=('Lucida Calligraphy',15),show="*").place(x=700,y=410)
        val1=StringVar()
        var=IntVar()
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        p.mainloop()
    def display1(self):
        def __init__(self, master):
                tk.Frame.__init__(self, master, height=10, width=10)
                self.entry = tk.Entry(self)
                self.entry.focus()
                self.entry.pack()
                self.clear_button = tk.Button(self, text="Clear text", command=self.clear_text)
                self.clear_button.pack()
    def clear_text(self):
            self.entry.delete(0, 'end')
    def main():
            root=tk.Tk()
            App(root).pack(expand=True, fill='both')
            x1=self.var1.get()
            y=self.var2.get()
            z=self.var3.get()
            x=self.var.get()
    def fnl(self):
        s=Toplevel(root)
        image1=PhotoImage(file="C:\\Users\\Student\\Desktop\\pic.png")
        s.config(background="#2B7878S")
        s.geometry("1550x700+0+0")
        l1=Label(s,image=image1).place(x=0, y=0)
        dayt=datetime.now()
        l2=Label(s,text=dayt,font=('times new roman',20),bg='pink').place(x=680,y=100)
        text=Text(s, height=25, width=105)
        text.tag_configure('bold_italica',font=('Lucida Calligraphy',12,'bold','italic'))
        text.tag_configure('big',font=('Lucida Calligraphy',24,'bold'))
        text.tag_configure('color',foreground='blue',font=('Lucida Calligraphy',14))
        text.tag_configure('groove',relief=GROOVE,borderwidth=2)
        text.tag_bind('bite','<l>',lambda e,t=text: t.insert(END, "TEXT" ))
        text.pack(side=LEFT)
        text.place(x=170,y=150)
        b1=Button(s,text="SAVE FOR TODAY",font=('times new roman',15),command=self.fnl,bg="pink",borderwidth=5,relief=RIDGE).place(x=500,y=580)
        s.mainloop()
root=Tk()
root.title("ONLINE  DIARY")
mb=diary(root)
root.mainloop()

