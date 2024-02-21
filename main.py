import time
from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import datetime

root  = Tk()
root.title('Log in')
root.geometry('925x500+300+200')
root.configure(bg = "#fff")
root.resizable(False,False)

def balancemenu():
    datainfile = pd.read_csv('data.csv')
    baldata =list((datainfile.to_dict()["BALANCE"]).values())
    window = Toplevel(root)
    window.title("TIMMER")
    window.geometry('925x500+300+200')
    window.configure(bg = "#fff")
    window.resizable(False,False)
    img = PhotoImage(file = "login.png")
    Label(window,image=img,bg = "white").place(x=50,y=50)
    frame = Frame(window,width=350,height=350,bg = "white")
    frame.place(x=480,y=70)
    heading = Label(frame,text= f"{baldata[virnum]}" , fg = "#57a1f8" , bg = 'WHITE' , font = ("MICROSOFT YaHei UI Light" , 23 , 'bold'))
    heading.place(x=100 , y=5)

    window.mainloop()


def transactiontimmer():
    window = Toplevel(root)
    window.title("TIMMER")
    window.geometry('925x500+300+200')
    window.configure(bg = "#fff")
    window.resizable(False,False)
    img = PhotoImage(file = "login.png")
    Label(window,image=img,bg = "white").place(x=50,y=50)
    frame = Frame(window,width=350,height=350,bg = "white")
    frame.place(x=480,y=70)
    heading = Label(frame,text= "NEXT TRANSACTION IN" , fg = "#57a1f8" , bg = 'WHITE' , font = ("MICROSOFT YaHei UI Light" , 12 , 'bold'))
    heading.place(x=100 , y=5)
    num = 5
    while num>0:
        heading = Label(frame,text=f"{num} SEC" , fg = "#57a1f8" , bg = 'WHITE' , font = ("MICROSOFT YaHei UI Light" , 13 , 'bold'))
        heading.place(x=100 , y=35)

        num -=1
        time.sleep(1)
        if num ==0 :
            window.destroy()
        window.update()
    window.mainloop()

def withdrawmenu():
    window = Toplevel(root)
    window.title("USER PANEL")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
    

    img = PhotoImage(file='login.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=50)
    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    heading=Label(frame,text='WITHDRAW',fg="#57a1f8",bg='white',font=('microsoft yeahei UI Light',23,'bold'))
    heading.place(x =100 , y =5)
    def on_enter(e):
        with_am.delete(0,'end')
    with_am = Entry(frame,width = 25 , fg = "black" , border = 0 , bg = "white" , font = ("MICROSOFT YaHei UI Light" , 11) )
    with_am.place(x= 30 , y=140)
    with_am.insert(0,"ENTER THE WITHDRAW AMOUNT(ONLY 100,200,2000 AVALABLE)")
    with_am.bind("<FocusIn>" , on_enter)
    with_am.bind("<FocusOut>" , on_leave)

    def tran():
        traamount = int(with_am.get())
        datainfile = pd.read_csv('data.csv')
        workingdata =datainfile.to_dict()
        temp = workingdata["BALANCE"][virnum]

        if temp - traamount <0:
            messagebox.showerror("ERROR", "INSUFFIENT BALANCE")
            transactiontimmer()
        
        else:
            workingdata["BALANCE"][virnum]=temp - traamount
            print(workingdata)

            current_time = datetime.datetime.now()

            transinfile = pd.read_csv('transactions.csv')
            workingtrans =transinfile.to_dict()
            a= list((transinfile.to_dict()["AMOUNT"]).values())
            workingtrans["ACCOUNT_HOLDER_NAME"][len(a)] = workingdata["ACCOUNT_HOLDER_NAME"][virnum]
            workingtrans["TRANSACTON_AMOUNT"][len(a)] = "-" + str(traamount)
            workingtrans["AMOUNT"][len(a)] = temp
            workingtrans["MODE OF TRANSACTION"][len(a)] = "WITHDRAW"
            workingtrans["BALANCE"][len(a)] = temp - traamount
            workingtrans["TIME"][len(a)] = current_time
            print(workingtrans)

            pd.DataFrame(workingdata).to_csv("data.csv" , index= False)

        
            pd.DataFrame(workingtrans).to_csv("transactions.csv" , index= False)
            window.destroy()
            transactiontimmer()

    Button(frame, width = 39 , pady = 7 , text='PROCEED',bg="#57a1f8",fg='white',border =0 ,command=tran ).place(x = 35 , y = 210)
    window.mainloop()

def depositmenu():
    window = Toplevel(root)
    window.title("USER PANEL")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
    

    img = PhotoImage(file='login.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=50)
    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    heading=Label(frame,text='WITHDRAW',fg="#57a1f8",bg='white',font=('microsoft yeahei UI Light',23,'bold'))
    heading.place(x =100 , y =5)
    def on_enter(e):
        with_am.delete(0,'end')
    with_am = Entry(frame,width = 25 , fg = "black" , border = 0 , bg = "white" , font = ("MICROSOFT YaHei UI Light" , 11) )
    with_am.place(x= 30 , y=140)
    with_am.insert(0,"ENTER THE DEPOSIT AMOUNT(ONLY 100,200,2000 AVALABLE)")
    with_am.bind("<FocusIn>" , on_enter)
    with_am.bind("<FocusOut>" , on_leave)

    def tran():
        traamount = int(with_am.get())
        datainfile = pd.read_csv('data.csv')
        workingdata =datainfile.to_dict()
        temp = workingdata["BALANCE"][virnum]
        workingdata["BALANCE"][virnum]=temp + traamount
        print(workingdata)

        current_time = datetime.datetime.now()

        transinfile = pd.read_csv('transactions.csv')
        workingtrans =transinfile.to_dict()
        a= list((transinfile.to_dict()["AMOUNT"]).values())
        workingtrans["ACCOUNT_HOLDER_NAME"][len(a)] = workingdata["ACCOUNT_HOLDER_NAME"][virnum]
        workingtrans["TRANSACTON_AMOUNT"][len(a)] = "+"+str(traamount)
        workingtrans["AMOUNT"][len(a)] = temp
        workingtrans["MODE OF TRANSACTION"][len(a)] = "DEPOSIT"
        workingtrans["BALANCE"][len(a)] = temp + traamount
        workingtrans["TIME"][len(a)] = current_time
        print(workingtrans)

        pd.DataFrame(workingdata).to_csv("data.csv" , index= False)
        pd.DataFrame(workingtrans).to_csv("transactions.csv" , index= False)

        window.destroy()
        transactiontimmer()

    Button(frame, width = 39 , pady = 7 , text='PROCEED',bg="#57a1f8",fg='white',border =0 ,command=tran ).place(x = 35 , y = 210)
    window.mainloop()

def graph():
    datainfile = pd.read_csv('data.csv')
    workingdata =datainfile.to_dict()
    temp = workingdata["ACCOUNT_HOLDER_NAME"][virnum]

    datainfile = pd.read_csv('transactions.csv')
    workingdata =datainfile.to_dict()
    print(workingdata)
    a= len(list((datainfile.to_dict()["AMOUNT"]).values()))
    x =[]
    y=[]
    count =0
    for i in range(a):
        if workingdata["ACCOUNT_HOLDER_NAME"][i] == temp :
            x.append(count)
            y.append(workingdata["BALANCE"][i])
            count +=1

    for i in range(len(x)):
        plt.annotate(f"{y[i]}" , (i,y[i]))
        plt.scatter(i,y[i])


    plt.plot(x,y , color = "blue" )
    plt.show()

def log_in():
    recusername = user.get()
    recpassword = (password.get())
    datainfile = pd.read_csv('data.csv')
    userdata =list((datainfile.to_dict()["USER_NAME"]).values())
    passwordata=list((datainfile.to_dict()["PASSWORD"]).values())
    test = False
    for i in range(0, len(userdata)):
        if userdata[i] == recusername:
            if passwordata[i] == recpassword :
                test = True
                index = i
        
    if test == False:
        messagebox.showerror("invalid" , "invalid Username or Password")
    
    if test :
        global virnum
        virnum = index
        ###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        window = Toplevel(root)
        window.title("USER PANEL")
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        img = PhotoImage(file='login.png')
        Label(window,image=img,border=0,bg='white').place(x=50,y=50)
        frame=Frame(window,width=350,height=390,bg='#fff')
        frame.place(x=480,y=50)
        heading=Label(frame,text='USER PANEL',fg="#57a1f8",bg='white',font=('microsoft yeahei UI Light',23,'bold'))
        heading.place(x =100 , y =5)
        def wi_out():
            window.destroy()
            withdrawmenu()
        def de_out():
            window.destroy()
            depositmenu()
        def bal_out():
            window.destroy()
            balancemenu()
        def ex_out():
            window.destroy()
            transactiontimmer()
        def gr_out():
            window.destroy()
            graph()
        
        
        Button(frame, width = 39 , pady = 7 , text='WITH DRAW',bg="#57a1f8",fg='white',border =0 , command= wi_out ).place(x = 35 , y = 70)

        Button(frame, width = 39 , pady = 7 , text='DEPOSIT',bg="#57a1f8",fg='white',border =0 ,command= de_out).place(x = 35 , y = 140)

        Button(frame, width = 39 , pady = 7 , text='CHECK BALANCE',bg="#57a1f8",fg='white',border =0 , command= bal_out ).place(x = 35 , y = 210)

        Button(frame, width = 39 , pady = 7 , text='EXIT',bg="#57a1f8",fg='white',border =0 , command= ex_out ).place(x = 35 , y = 280)

        Button(frame, width = 39 , pady = 7 , text='GRAPH BALANCE',bg="#57a1f8",fg='white',border =0 , command= gr_out ).place(x = 35 , y = 350)

        window.mainloop()


        ###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
img = PhotoImage(file = "sbi1.png")
Label(root,image=img,bg = "white").place(x=50,y=50)
frame = Frame(root,width=350,height=350,bg = "white")
frame.place(x=480,y=70)
heading = Label(frame,text="LOG IN" , fg = "#57a1f8" , bg = 'WHITE' , font = ("MICROSOFT YaHei UI Light" , 23 , 'bold'))
heading.place(x=100 , y=5)
###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
###:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name= user.get()
    if name =='':
        user.insert(0,'username')
user = Entry(frame,width = 25 , fg = "black" , border = 0 , bg = "white" , font = ("MICROSOFT YaHei UI Light" , 11) )
user.place(x= 30 , y=80)
user.insert(0,"username")
user.bind("<FocusIn>" , on_enter)
user.bind("<FocusOut>" , on_leave)
Frame(frame, width = 295 , height =2 , bg = "black").place(x = 25 , y = 107)
###::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    name= password.get()
    if name =='':
        password.insert(0,'password')
password = Entry(frame,width = 25 , fg = "black" , border = 0 , bg = "white" , font = ("MICROSOFT YaHei UI Light" , 11) )
password.place(x= 30 , y=150)
password.insert(0,"password")
password.bind("<FocusIn>" , on_enter)
password.bind("<FocusOut>" , on_leave)
Frame(frame, width = 295 , height =2 , bg = "black").place(x = 25 , y = 177)
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Button(frame , width=39 , pady = 7 , text = "LOG IN" , bg = "#57a1f8" , fg = "white" , border =0 , command= log_in).place(x =35 , y= 204)

root.mainloop()










