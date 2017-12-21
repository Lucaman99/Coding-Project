#This program communicates with a local MySQL database on my computer.
import Tkinter as tk
from Tkinter import *
import random
import math
from datetime import datetime
import time
import MySQLdb
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

db = MySQLdb.connect(host="localhost", user="root", passwd="#Your password goes here", db="signup_login")

def get(event):
	variableone = e1.get()
	variabletwo = e2.get()
	variablethree = e3.get()
	variablefour = e4.get()
	variablefive = e5.get()
	truth_bool = bool(variableone == "" or variabletwo == "" or variablethree == "" or variablefive == "" or variablefour == "")
	if truth_bool == False:
		rand = random.randint(10000,99999)
		adr = "messagingconfirm99@gmail.com"
		toadr = variablethree
		msg = MIMEMultipart()
		msg['From'] = adr
		msg['To'] = toadr
		msg['Subject'] = "Apogee Messaging Confirmation Email"
		body = "Thank you for signing up for Apogee Messaging. This is your 5-digit confirmation code: "+str(rand)
		msg.attach(MIMEText(body, 'plain'))
		serv = smtplib.SMTP('smtp.gmail.com', 587)
		serv.ehlo()
		serv.starttls()
		serv.ehlo()
		serv.login("messagingconfirm99@gmail.com", "#Your password goes here")
		txt = msg.as_string()
		serv.sendmail(adr, toadr, txt)
		serv.quit()
		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e4.delete(0, END)
		e5.delete(0, END)
		e1.insert(0, "")
		e2.insert(0, "")
		e3.insert(0, "")
		e4.insert(0, "")
		e5.insert(0, "")
		root.destroy()
		mas = Tk()
		mas.minsize(width=500, height=500)
		mas.maxsize(width=500, height=500)
		mas.config(bg="#33618E", pady=40, padx=65)
		Label(mas, bg="#33618E").grid(row=0)
		ac = Label(mas, text="Confirmation Code", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white")
		ac.grid(row=1)
		k1 = Entry(mas)
		k1.grid(row=1, column=1)
		def verify(event):
			varg = k1.get()
			print(varg)
			print(str(rand))
			if varg == str(rand):
				print("Your confirmation code has been verified. Your account is now valid.")
				exe = db.cursor()
				exe.execute("INSERT INTO user_info (email, username, password, firstname, lastname) VALUES ('%s', '%s', '%s', '%s', '%s')" % (variablethree, variableone, variabletwo, variablefour, variablefive))
				db.commit()
				db.close()
			else:
				print("Acess Denied")
		k1.bind("<Return>", verify)

def login():
	root.destroy()
	master = Tk()
	master.minsize(width=500, height=500)
	master.maxsize(width=500, height=500)
	master.config(bg="#33618E", pady=40, padx=65)
	Label(master, text="Apogee Messaging Sign-Up", bg="#33618E", font="Calibri 30 bold", fg="white").grid(row=0, column=0, columnspan=3)
	Label(master, bg="#33618E").grid(row=1)
	Label(master, bg="#33618E").grid(row=2)
	Label(master, bg="#33618E").grid(row=3)
	Label(master, bg="#33618E").grid(row=4)
	Label(master, bg="#33618E").grid(row=5)
	a = Label(master, text="Username", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white")
	a.grid(row=6)
	b = Label(master, text="Password", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white" )
	b.grid(row=7)

	def find(event):
		var1 = l1.get()
		var2 = l2.get()
		other = db.cursor()
		other.execute("SELECT * FROM user_info")
		userarr = []
		passarr = []
		for row in other.fetchall():
			userarr.append(row[1])
			passarr.append(row[2])
		if var1 not in userarr or var2 not in passarr:
			print("Acess Denied")
		else:
			userindex = userarr.index(var1)
			passindex = passarr.index(var2)
			if userindex == passindex:
				print("Access Granted")
			else:
				print("Acess Denied")
		print(var1)
		print(var2)
		print(userarr)
		print(passarr)

	l1 = Entry(master)
	l2 = Entry(master, show="*")

	l1.bind("<Return>", find)
	l2.bind("<Return>", find)

	l1.grid(row=6, column=1)
	l2.grid(row=7, column=1)

	mainloop( )

root = Tk()
Label(root, text="Apogee Messaging Log-In", bg="#33618E", font="Calibri 30 bold", fg="white").grid(row=0, column=0, columnspan=3)
Label(root, bg="#33618E").grid(row=2)
Label(root, bg="#33618E").grid(row=3)
Label(root, bg="#33618E").grid(row=4)
four = Label(root, text="Email", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white")
four.grid(row=6)
one = Label(root, text="Username", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white")
one.grid(row=7)
two = Label(root, text="Password", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white" )
two.grid(row=8)
five = Label(root, text="First Name", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white")
five.grid(row=9)
six = Label(root, text="Last Name", padx=10, justify=tk.LEFT, pady=10, bg="#33618E", font="Calibri 20 bold", fg="white")
six.grid(row=10)
Label(root, bg="#33618E").grid(row=11)
three = Label(root, text="Log-In Here", font="Calibri 20 bold", fg="white", bg="#33618E").grid(row=12, columnspan=1, column=0)
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
root.config(bg="#33618E", pady=40, padx=65)

e1 = Entry(root)
e2 = Entry(root, show="*")
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)

e1.bind("<Return>", get)
e2.bind("<Return>", get)
e3.bind("<Return>", get)
e4.bind("<Return>", get)
e5.bind("<Return>", get)

e1.grid(row=7, column=1)
e2.grid(row=8, column=1)
e3.grid(row=6, column=1)
e4.grid(row=9, column=1)
e5.grid(row=10, column=1)
t = Button(text="Log-In", highlightbackground='#33618E', padx=75, command=login)
t.grid(row=12, column=1)

mainloop( )
