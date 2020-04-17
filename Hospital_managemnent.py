
from pymysql import *
a=connect('localhost','root','Salsabeel@70','Hospital')
b=a.cursor()


from tkinter import *
root=Tk()
root.title('Hospital Appointment Management')
root.geometry('700x500')

L1=Label(root,text="Hospital Appointment Management System",font=('bold',30))
L1.place(x=50,y=20)

L2=Label(root,text='Patient_Name:',font=('bold',15))
L2.place(x=20,y=80)

s=StringVar()
e1=Entry(root,textvariable=s)
e1.place(x=160,y=90)

L2=Label(root,text='Age',font=('bold',15))
L2.place(x=20,y=120)

s2=StringVar()
e2=Entry(root,textvariable=s2)
e2.place(x=160,y=120)

L3=Label(root,text='Gender',font=('bold',15))
L3.place(x=20,y=160)

s3=StringVar()
e3=Entry(root,textvariable=s3)
e3.place(x=160,y=160)

L4=Label(root,text='Appoint_time:',font=('bold',15))
L4.place(x=20,y=200)

s4=StringVar()
e4=Entry(root,textvariable=s4)
e4.place(x=160,y=200)

L5=Label(root,text='Phone_number:',font=('bold',15))
L5.place(x=20,y=240)

s5=StringVar()
e5=Entry(root,textvariable=s5)
e5.place(x=160,y=240)



def fun():
    print(e1.get())
    print(e2.get())
    print(e3.get())
    print(e4.get())
    print(e5.get())
    b.execute("insert into submit values('{}','{}','{}','{}','{}','{}')".format(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
    a.commit()

b1=Button(root,text="Submit",bg="red",fg="white")
b1.place(x=120,y=290)






