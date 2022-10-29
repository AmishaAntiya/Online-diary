from tkinter import *
root=Tk()
c=Canvas(root,bg='sky blue',height=2000,width=2000)
l=c.create_line(0,0,100,100,fill='red',activefill='purple')
r=c.create_rectangle(400,335,700,500,fill='green')
o=c.create_oval(100,100,400,335,fill='yellow')
p=c.create_polygon(200,750,300,600,700,700,fill='red')
t=c.create_text(1000,150,text='HELLO')
i=PhotoImage(file='pic.png')
#i1=PhotoImage(file='')
c.create_image(700,750,anchor=SW,image=i)
c.pack()
root.mainloop()

