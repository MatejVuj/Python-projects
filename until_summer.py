import datetime
from time import strftime
import tkinter
from tkinter import*
import tkinter as tk
from tkinter import ttk 

#funkcija za ispis danjasnjeg datuma u prvom labelu
def today_date():

    date1 = datetime.datetime.now()
    date2 = date1.strftime("%d - %m - %Y")

    return date2

#funkcija za provjeru je li godina prijestupna
def is_year_leap():

    year = datetime.datetime.now()
    year =int(year_now.strftime("%Y"))

    if (year % 4 == 0):
        print("prijestupna", year)
        return True
    
    elif (year % 4 != 0):
        print("NIJE prijestupna", year)
        return False

#funkcija za racunanje i update progress bara
def progress_bar_update():
    
    days_in_year = 365
    months_in_year = 12
    weeks_in_year = 52

    #namistanje varijabli za datume
    day_before_autumn = 264
    first_day_of_summer = 172
    number_of_days_between_fall_and_summer = 101
    number_of_days_between_fall_and_summer_leap_year = 102

    #danjasnji dan
    today = datetime.datetime.now()
    today.strftime("%j")
    today = int(today.strftime("%j"))

    #isto danasnji dan
    day_in_year = datetime.datetime.now()
    day_in_year.strftime("%j")
    day_in_year = int (day_in_year.strftime("%j"))

    #za prijestupnu godinu
    if(is_year_leap() == True):

        if ( today > day_before_autumn ):
            progress = day_in_year - (day_before_autumn + 1)
            print(progress)
            return progress

        elif ( day_in_year > 1 and day_in_year < (first_day_of_summer + 1) ):
            progress = day_in_year + number_of_days_between_fall_and_summer_leap_year
            print("mirko")
            return progress

    #za noramlnu godinu
    elif(is_year_leap() == False):

        if ( today > day_before_autumn ):
            progress = day_in_year - day_before_autumn
            print(progress)
            return progress

        elif ( day_in_year > 1 and day_in_year < first_day_of_summer ):
            progress = day_in_year + number_of_days_between_fall_and_summer
            print("mirko")
            return progress
            

#neka funkcija za misece
def number_of_months():
    month = datetime.datetime.now()
    num_month = month.strftime("%m")
    num_month = num_month - 1
    return num_month

#funkcija za provjeru login
def login_fun(login):

    #uzimanje napisanog iz enrya definiranih u login
    Name = name.get()
    Surname = surname.get()
    Password = password.get()

    if(Name == "Matej" and Surname == "Vujevic" and Password == "Solin"):
        print(Name, Surname, Password)
        login.destroy()

    else:
        pass
    
#funkcija za SingUp
def singup_fun(login):
    pass


open = True;

login = Tk()

#naslov prozora korisniku
l1 = Label(login, text = "Login or SingUp").grid(row = 0, column = 1)

#postavljanje labela da se zna koji je netry za sta
Label(login, text='First Name').grid(row=1)
Label(login, text='Last Name').grid(row=2)
Label(login, text='Password').grid(row=3) 

#postavljanje entrija zas prijavu
name = Entry(login,)
surname = Entry(login,)
password = Entry(login)
name.grid(row=1, column=1)
surname.grid(row=2, column=1)
password.grid(row=3, column=1)

Login_button = tk.Button(login, text = "Login", width = 15, command = lambda login=login:login_fun(login)).grid(row = 5, column = 0)

Signup_button = tk.Button(login, text = "Sign Up", width = 15, command = lambda login=login:singup_fun(login)).grid(row = 5, column = 1) 

login.mainloop()

root = Tk()
#ispis danasnjeg datuma
w = Label(root, text = "Till Summer")
w.pack()

#ISPIS DANASNJEG DATUMA
date = Label(root, text = today_date())
date.pack()

#Progress Bar za punjenje
year_now = datetime.datetime.now()
year = int(year_now.strftime("%Y"))

today = datetime.datetime.now()

beginning_summer = datetime.datetime(year, 6, 21)
end_summer = datetime.datetime(year, 9, 22)

if(is_year_leap() == True):
    progress = ttk.Progressbar(root, orient = "horizontal", length=273, mode="determinate",
                            maximum = 366)

    if today >= beginning_summer and today < end_summer:
        progress.step(273)
        progress.pack(pady=20)

    else: 
        progress.step(progress_bar_update())
        progress.pack(pady=20)

elif(is_year_leap() == False):
    progress = ttk.Progressbar(root, orient = "horizontal", length=272, mode="determinate",
                            maximum = 365)

    if today >= beginning_summer and today < end_summer:
        progress.step(272)
        progress.pack(pady=20)

    else: 
        progress.step(progress_bar_update())
        progress.pack(pady=20)


passed_days = Label(root, text = progress_bar_update())
passed_days.pack()

root.mainloop()