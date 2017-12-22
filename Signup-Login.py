# Python 3
# This program communicates with a local MySQL database on my computer.
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from random import randint
import MySQLdb
import smtplib
# import math
# from datetime import datetime
# import time

db = MySQLdb.connect(host='localhost', user='root', passwd='DB PASSWORD', db='signup_login')


def get(event):
    variable_one = e1.get()
    variable_two = e2.get()
    variable_three = e3.get()
    variable_four = e4.get()
    variable_five = e5.get()
    es = [e1, e2, e3, e4, e5]
    variables = [variable_one, variable_two, variable_three, variable_four]
    # truth_bool = bool(
    #     variableone == "" or variabletwo == "" or variablethree == "" or variablefive == "" or variablefour == "")
    # if not truth_bool:
    if variables.count('') < 4:  # do you want to check variable_five or not?
        rand = randint(10000, 99999)  # do you want to do a random number or a random code? eg: 0EF9I
        adr = 'messagingconfirm99@gmail.com'
        to_adr = variable_three
        msg = MIMEMultipart()
        msg['From'] = adr
        msg['To'] = to_adr
        msg['Subject'] = 'Apogee Messaging Confirmation Email'
        body = 'Thank you for signing up for Apogee Messaging. This is your 5-digit confirmation code: ' + str(rand)
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('messagingconfirm99@gmail.com', 'EMAIL PASSWORD')
        txt = msg.as_string()
        s.sendmail(adr, to_adr, txt)
        s.quit()
        for e in es:
            e.delete(0, END)
            e.insert(0, '')
        # e1.delete(0, END)
        # e2.delete(0, END)
        # e3.delete(0, END)
        # e4.delete(0, END)
        # e5.delete(0, END)
        # e1.insert(0, "")
        # e2.insert(0, "")
        # e3.insert(0, "")
        # e4.insert(0, "")
        # e5.insert(0, "")
        root.destroy()
        mas = Tk()
        mas.minsize(width=500, height=500)
        mas.maxsize(width=500, height=500)
        mas.config(bg='#33618E', pady=40, padx=65)
        Label(mas, bg='#33618E').grid(row=0)
        ac = Label(mas, text='Confirmation Code', padx=10, justify=tk.LEFT, pady=10, bg='#33618E',
                   font='Calibri 20 bold', fg='white')
        ac.grid(row=1)
        k1 = Entry(mas)
        k1.grid(row=1, column=1)

        def verify(event):
            var_g = k1.get()
            print(var_g)
            print(str(rand))
            if var_g == str(rand):
                print('Your confirmation code has been verified. Your account is now valid.')
                exe = db.cursor()
                exe.execute(
                    "INSERT INTO user_info (email, username, password, firstname, lastname) VALUES ('%s', '%s', '%s', "
                    "'%s', '%s')" % (
                        variable_three, variable_one, variable_two, variable_four, variable_five))
                db.commit()
                db.close()
            else:
                print('Access Denied')

        k1.bind('<Return>', verify)


def login():
    root.destroy()
    master = Tk()
    master.minsize(width=500, height=500)
    master.maxsize(width=500, height=500)
    master.config(bg='#33618E', pady=40, padx=65)
    Label(master, text='Apogee Messaging Sign-Up', bg='#33618E', font='Calibri 30 bold', fg='white').grid(row=0,
                                                                                                          column=0,
                                                                                                          columnspan=3)
    Label(master, bg='#33618E').grid(row=1)
    Label(master, bg='#33618E').grid(row=2)
    Label(master, bg='#33618E').grid(row=3)
    Label(master, bg='#33618E').grid(row=4)
    Label(master, bg='#33618E').grid(row=5)
    a = Label(master, text="Username", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold",
              fg="white")
    a.grid(row=6)
    b = Label(master, text="Password", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold",
              fg="white")
    b.grid(row=7)

    def find(event):
        var1 = l1.get()
        var2 = l2.get()
        other = db.cursor()
        other.execute('SELECT * FROM user_info')
        user_arr = []
        pass_arr = []
        for row in other.fetchall():
            user_arr.append(row[2])
            pass_arr.append(row[3])
        if var1 not in user_arr or var2 not in pass_arr:
            print('Access Denied')
        else:
            # user_index = user_arr.index(var1)
            # pass_index = pass_arr.index(var2)
            # if user_index == pass_index:
            if user_arr.index(var1) == pass_arr.index(var2):
                print('Access Granted')
            else:
                print('Access Denied')

    l1 = Entry(master)
    l2 = Entry(master, show="*")

    l1.bind('<Return>', find)
    l2.bind('<Return>', find)

    l1.grid(row=6, column=1)
    l2.grid(row=7, column=1)

    mainloop()


root = Tk()
Label(root, text='Apogee Messaging Log-In', bg='#33618E', font='Calibri 30 bold', fg='white').grid(row=0, column=0,
                                                                                                   columnspan=3)
Label(root, bg='#33618E').grid(row=2)
Label(root, bg='#33618E').grid(row=3)
Label(root, bg='#33618E').grid(row=4)
four = Label(root, text='Email', padx=10, justify=tk.LEFT, pady=10, bg='#33618E', font='Calibri 30 bold', fg='white')
four.grid(row=6)
one = Label(root, text='Username', padx=10, justify=tk.LEFT, pady=10, bg='#33618E', font='Calibri 30 bold', fg='white')
one.grid(row=7)
two = Label(root, text='Password', padx=10, justify=tk.LEFT, pady=10, bg='#33618E', font='Calibri 30 bold', fg='white')
two.grid(row=8)
five = Label(root, text='First Name', padx=10, justify=tk.LEFT, pady=10, bg='#33618E', font='Calibri 30 bold',
             fg='white')
five.grid(row=9)
six = Label(root, text='Last Name', padx=10, justify=tk.LEFT, pady=10, bg='#33618E', font='Calibri 30 bold', fg='white')
six.grid(row=10)
Label(root, bg='#33618E').grid(row=11)
three = Label(root, text='Log-In Here', bg='#33618E', font='Calibri 30 bold', fg='white').grid(row=12, columnspan=1,
                                                                                               column=0)
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
root.config(bg='#33618E', pady=40, padx=65)

e1 = Entry(root)
e2 = Entry(root, show='*')
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)

e1.bind('<Return>', get)
e2.bind('<Return>', get)
e3.bind('<Return>', get)
e4.bind('<Return>', get)
e5.bind('<Return>', get)

e1.grid(row=7, column=1)
e2.grid(row=8, column=1)
e3.grid(row=6, column=1)
e4.grid(row=9, column=1)
e5.grid(row=10, column=1)
t = Button(text='Log-In', highlightbackground='#33618E', padx=75, command=login)
t.grid(row=12, column=1)

mainloop()
