

#import pymysql
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class bank():
    def __init__(self,root):
        self.root=root
        self.root.title("Bank Management")


        scrn_width=self.root.winfo_screenwidth()
        scrn_height=self.root.winfo_screenheight()
        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")

        mainLabel=tk.Label(self.root,text="Bank Account Management System",font=("Arial",40,"bold"),bg="light green",bd=5,relief="groove")
        mainLabel.pack(side="top",fill="x")
        mainframe=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        mainframe.place(x=400,y=90,width=450,height=550)

 
        openAcBtn=tk.Button(mainframe,command=self.openAc,width=20,text="Open Account",bg="light blue",bd=3,relief="raised",font=("Arial",20,"bold"))
        openAcBtn.grid(row=0,column=0,padx=40,pady=65)

        depBtn=tk.Button(mainframe,command=self.deposit,width=20,text="Deposit",bg="light blue",bd=3,relief="raised",font=("Arial",20,"bold"))
        depBtn.grid(row=1,column=0,padx=40,pady=65)

        wdBtn=tk.Button(mainframe,command=self.wd,width=20,text="WithDraw",bg="light blue",bd=3,relief="raised",font=("Arial",20,"bold"))
        wdBtn.grid(row=2,column=0,padx=40,pady=65)

    def openAc(self):
        self.openAcFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.openAcFrame.place(x=400,y=90,width=450,height=550)

        uNameLabel=tk.Label(self.openAcFrame,text="User Name",bg="light gray",font=("Arial",15,"bold"))
        uNameLabel.grid(row=0,column=0,padx=20,pady=30)
        self.uNameIn=tk.Entry(self.openAcFrame,width=15,font=("Arial",15))
        self.uNameIn.grid(row=0,column=1,padx=5,pady=30)

        
        uPWLabel=tk.Label(self.openAcFrame,text="Enter Password",bg="light gray",font=("Arial",15,"bold"))
        uPWLabel.grid(row=1,column=0,padx=20,pady=30)
        self.uPWIn=tk.Entry(self.openAcFrame,width=15,font=("Arial",15))
        self.uPWIn.grid(row=1,column=1,padx=5,pady=30)


        confirmLabel=tk.Label(self.openAcFrame,text="Confirm Password",bg="light gray",font=("Arial",15,"bold"))
        confirmLabel.grid(row=2,column=0,padx=20,pady=30)
        self.confirmIn=tk.Entry(self.openAcFrame,width=15,font=("Arial",15))
        self.confirmIn.grid(row=2,column=1,padx=5,pady=30)


        okBtn=tk.Button(self.openAcFrame,command=self.insert,text="OK",width=10,bg="light blue",bd=3,relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=3,column=0,padx=40,pady=120)

        closeBtn=tk.Button(self.openAcFrame,command=self.close_openAc,text="Close",width=10,bg="light blue",bd=3,relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=3,column=1,padx=40,pady=120)

    def close_openAc(self):
        self.openAcFrame.destroy()

    def insert(self):
        uName=self.uNameIn.get()
        uPW=self.uPWIn.get()
        confirm=self.confirmIn.get()

        if uPW==confirm:
            con = mysql.connector.connect(host="localhost",user="root",password="Password",database="bankdb")
            cur = con.cursor()
            cur.execute("INSERT INTO account (userName,userPW) values(%s,%s)",(uName,uPW))
            con.commit()
            cur.close()
            con.close()

            tk.messagebox.showinfo("Success","Account Opened Successfully!.")
            self.clear()
        else:
            tk.messagebox.showerror("Error","Both Passwords should same!")
            self.clear()
    def clear(self):
        self.uNameIn.delete(0,tk.END)
        self.uPWIn.delete(0,tk.END)
        self.confirmIn.delete(0,tk.END)

    def deposit(self):
        self.depFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.depFrame.place(x=400,y=90,width=450,height=550)

        NameLabel=tk.Label(self.depFrame,text="User Name",bg="light gray",font=("Arial",15,"bold"))
        NameLabel.grid(row=0,column=0,padx=20,pady=30)
        self.NameIn=tk.Entry(self.depFrame,width=15,font=("Arial",15))
        self.NameIn.grid(row=0,column=1,padx=5,pady=30)

        amountLabel=tk.Label(self.depFrame,text="Enter Amount:",bg="light gray",font=("Arial",15,"bold"))
        amountLabel.grid(row=1,column=0,padx=20,pady=30)
        self.amountIn=tk.Entry(self.depFrame,width=15,font=("Arial",15))
        self.amountIn.grid(row=1,column=1,padx=5,pady=30)

        okBtn=tk.Button(self.depFrame,command=self.deposit_fun,text="Deposit",width=10,bg="light blue",bd=3,relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=2,column=0,padx=40,pady=150)

        closeBtn=tk.Button(self.depFrame,command=self.close_deposit,text="Close",width=10,bg="light blue",bd=3,relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=2,column=1,padx=40,pady=150)

    def deposit_fun(self):
        name=self.NameIn.get()
        amount=int(self.amountIn.get())

        con = mysql.connector.connect(host="localhost",user="root",password="Password",database="bankdb")
        cur = con.cursor()
        cur.execute("select balance from account where userName=%s",name)
        data=cur.fetchone()
        if data:
            update=data[0]+amount
            cur.execute("update account set balance=%s where userName=%s",(update,name,))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","OPeration was Successfully!.")

        else:
            tk.messagebox.showerror("Error","Invalid Customer Name")

    def close_deposit(self):
        self.depFrame.destroy()




    def wd(self):
        self.wdFrame=tk.Frame(self.root,bg="light gray",bd=5,relief="ridge")
        self.wdFrame.place(x=400,y=90,width=450,height=550)

        cNameLabel=tk.Label(self.wdFrame,text="User Name",bg="light gray",font=("Arial",15,"bold"))
        cNameLabel.grid(row=0,column=0,padx=20,pady=30)
        self.cNameIn=tk.Entry(self.wdFrame,width=15,font=("Arial",15))
        self.cNameIn.grid(row=0,column=1,padx=5,pady=30)

        
        cPWLabel=tk.Label(self.wdFrame,text="Enter Password",bg="light gray",font=("Arial",15,"bold"))
        cPWLabel.grid(row=1,column=0,padx=20,pady=30)
        self.cPWIn=tk.Entry(self.wdFrame,width=15,font=("Arial",15))
        self.cPWIn.grid(row=1,column=1,padx=5,pady=30)


        wdLabel=tk.Label(self.wdFrame,text="Enter amount",bg="light gray",font=("Arial",15,"bold"))
        wdLabel.grid(row=2,column=0,padx=20,pady=30)
        self.wdIn=tk.Entry(self.wdFrame,width=15,font=("Arial",15))
        self.wdIn.grid(row=2,column=1,padx=5,pady=30)


        okBtn=tk.Button(self.wdFrame,command=self.wd_fun,text="WithDraw",width=10,bg="light blue",bd=3,relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=3,column=0,padx=40,pady=120)

        closeBtn=tk.Button(self.wdFrame,command=self.close_wd,text="Close",width=10,bg="light blue",bd=3,relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=3,column=1,padx=40,pady=120)

    def wd_fun(self):
        name=self.cNameIn.get()
        pw=self.cPWIn.get()
        amount=int(self.wdIn.get())
        #data=cur.fetchone

        
        con = mysql.connector.connect(host="localhost",user="root",password="Password",database="bankdb")
        cur = con.cursor()
        cur.execute("select userPW,balance from account where userName=%s",name)
        data=cur.fetchon()
        if data:
            if data[0]==pw:

                if data[1]>=amount:
                    
                    update=data[1]-amount
                    cur.execute("update account set balance=%s where userName=%s",(update,name))

                    con.commit()
                    cur.close()
                    con.close()
                    tk.messagebox.showinfo("Success","OPeration was Success")

                else:
                    tk.messagebox.showerror("Error","Insufficient balance!")

            else:
                tk.messagebox.showerror("Error","Invalid Customer Name!")



        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")

            
        con.commit()
        cur.close()
        con.close()

        tk.messagebox.showinfo("Success","Account Opened Successfully!.")
        self.clear()



    def close_wd(self):
        self.wdFrame.destroy()

root=tk.Tk()
obj=bank(root)
root.mainloop()
     

"""

import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="bankdb"
)

# Create a cursor
cur = conn.cursor()

# Execute the SQL command
cur.execute("INSERT INTO account (username, userpw, balance) VALUES ('poojita', 'pooja21', 8000)")

# Commit the changes



# Close the cursor and connection
cur.close()
conn.close()
"""