from tkinter import *
from tkinter import messagebox
import expensedb
import os
import time
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure

root = Tk()
root.title("Expenese Manager")
root.geometry("450x450")


def insert_exp_values():
    val = (t_date.get(),t_amount.get(),t_description.get(),clicked.get())
    expensedb.exp_values(val)

    t_date.delete(0, END)
    t_amount.delete(0, END)
    t_description.delete(0, END)
    

def insert_inc_values():
    val = (t_date.get(),t_amount.get(),t_description.get(), clicked.get())
    expensedb.inc_values(val)
    
    t_date.delete(0, END)
    t_amount.delete(0, END)
    t_description.delete(0, END)
    
    
    
def insert_plan_values():
    if t_expp.get():
        
        val = (date.today(),t_expp.get(),t_incp.get())
        expensedb.plan_values(val)
    
        t_expp.delete(0, END)
        t_incp.delete(0, END)
    else:
        messagebox.showerror("error", "Enter valid values")
    
    
#to open expense window
def expense_window():
    global t_date,t_amount, t_description, clicked
    new_window = Toplevel(root)
    new_window.title("Expenses")
    new_window.geometry("400x400")
    
    #labels
    l_date = Label(new_window, text = "Date",height = 3,width=10, anchor = 'w')
    l_amount = Label(new_window, text = "Amount",height = 3,width=10, anchor = 'w')
    l_description = Label(new_window, text = "Description",height = 3,width=10, anchor = 'w')
    l_category = Label(new_window, text = "Category",height = 3,width=10, anchor = 'w')

    #textboxes
    t_date = Entry(new_window, width = 30)
    t_amount = Entry(new_window, width = 30)
    t_description = Entry(new_window, width = 30)
    #t_category = Entry(new_window, width = 30)

    #category dropdown
    options = ['Food','Gifts','Health/Medical',
               'Home','Transporyation','Personal',
               'Pets','Utilities','Travel','Debt','Other']
    clicked = StringVar()
    clicked.set('Food')
    d_category = OptionMenu(new_window, clicked, *options)

    #submit button
    s_btn = Button(new_window, text="Submit", width = 10,command = insert_exp_values)

    #placing labels
    l_date.grid(row=0, column=0)
    l_amount.grid(row=1, column=0)
    l_description.grid(row=2, column=0)
    l_category.grid(row=3, column=0)

    #placing textboxes
    t_date.grid(row=0, column=1)
    t_amount.grid(row=1, column=1)
    t_description.grid(row=2, column=1)
    d_category.grid(row=3, column=1)

    #placing submit button
    s_btn.grid(row=4,column=1)

#to open income window
def income_window():
    global t_date, t_amount, t_description, clicked
    new_window = Toplevel(root)
    new_window.title("Income")
    new_window.geometry("400x400")
    
    #labels
    l_date = Label(new_window, text = "Date",height = 3,width=10, anchor = 'w')
    l_amount = Label(new_window, text = "Amount",height = 3,width=10, anchor = 'w')
    l_description = Label(new_window, text = "Description",height = 3,width=10, anchor = 'w')
    l_category = Label(new_window, text = "Category",height = 3,width=10, anchor = 'w')

    #textboxes
    t_date = Entry(new_window, width = 30)
    t_amount = Entry(new_window, width = 30)
    t_description = Entry(new_window, width = 30)
    #d_category = Entry(new_window, width = 30)

    #category dropdown
    options = ['Savings','Paycheck','Bonus',
               'Interest','Other']
    clicked = StringVar()
    clicked.set('Paycheck')
    d_category = OptionMenu(new_window, clicked, *options)

    #submit button
    s_btn = Button(new_window, text="Submit", command = insert_inc_values, width = 10)

    #placing labels
    l_date.grid(row=0, column=0)
    l_amount.grid(row=1, column=0)
    l_description.grid(row=2, column=0)
    l_category.grid(row=3, column=0)

    #placing textboxes
    t_date.grid(row=0, column=1)
    t_amount.grid(row=1, column=1)
    t_description.grid(row=2, column=1)
    d_category.grid(row=3, column=1)

    #placing submit button
    s_btn.grid(row=4,column=1)

#to open report window
def report_window():
    month = date.today().month
    new_window = Toplevel(root)
    new_window.title("Report")
    new_window.geometry("600x600")
    options = [1,2,3,4,5,6,7,8,9,10,11,12]
    clicked = StringVar()
    clicked.set(month)
    print(clicked.get())
    #dropdown
    drop = OptionMenu(new_window, clicked, *options)
    drop.grid(row=0, column=0)

    #Label(new_window, text=date.today()).grid(row=0, column=0)
    #bar chart of planned expense and actual expense
    plan_expense = expensedb.plan_exp(clicked.get())
    total_expense = expensedb.total_exp(clicked.get())
    
    
    fig1, (ax1, ax2) = plt.subplots(1,2, figsize=(6,3))
    ax1.bar(['plan_expense','total_expense'],[plan_expense[0][0],total_expense[0][0]],
            width = 0.3)
    ax1.set_title("Expense")
    
    
    canvas = FigureCanvasTkAgg(fig1, master = new_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 1, column = 0)
    print(total_expense[0][0])
    print(plan_expense[0][0])


    #bar chart of planned income and actual income
    plan_income = expensedb.plan_inc(month)
    total_income = expensedb.total_inc(month)
    print(plan_income[0][0])
    print(total_income[0][0])


    #pie chart for expense and income by category
    income_cat = expensedb.income_cat(clicked.get())
    expense_cat = expensedb.expense_cat(clicked.get())

    #income
    category_inc = []
    amount_inc = []
    for row in income_cat:
        category_inc.append(row[0])
        amount_inc.append(int(row[1]))

    #expense
    category_exp = []
    amount_exp = []
    for row in expense_cat:
        category_exp.append(row[0])
        amount_exp.append(int(row[1]))

    print(category_exp)
    print(amount_exp)
    ax2.bar(['plan_income','total_income'],[plan_income[0][0],total_income[0][0]],
            width = 0.3)
    ax2.set_title("Income")
    fig1.tight_layout()
    #canvas = FigureCanvasTkAgg(fig1, master = new_window)
    #canvas.draw()
    #canvas.get_tk_widget().grid(row = 0, column = 1)

    #pie chart of income
    fig2, (ax1,ax2) = plt.subplots(1,2, figsize=(6,3))
    ax1.pie(amount_exp, labels = category_exp, autopct = '%1.1f%%', shadow = True)
    ax1.set_title("expense by category")
    ax2.pie(amount_inc, labels = category_inc, autopct = '%1.1f%%', shadow = True)
    ax2.set_title("income by category")
    fig2.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig2, master = new_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 2, column = 0)    
    



#expense planned
l_expp = Label(root, text = "Expense Planned",padx=5,pady=5)
t_expp = Entry(root, width = 30)
l_expp.grid(row=1, column=0 )
t_expp.grid(row=1, column=1)

#income planned
l_incp = Label(root, text = "Income Planned",padx=5,pady=5)
t_incp = Entry(root, width = 30)
l_incp.grid(row=2, column=0 )
t_incp.grid(row=2, column=1)


#display image
img = PhotoImage(file=r'C:\Users\varun\OneDrive\Desktop\project\paisa.png')
img1 = img.subsample(3,3)
Label(root, image = img1).grid(row = 0, column = 0,columnspan = 2,padx = 5, pady = 5)

#expense button
expense_btn = Button(root, text = "Expenses",width = 10 , padx = 5, pady = 5,command = expense_window)
expense_btn.grid(row=3, column=0 )

#income button
income_btn = Button(root, text = "Income",width = 10 ,padx = 5, pady = 5, command = income_window)
income_btn.grid(row=4, column=0 )

#report button
report_btn = Button(root, text = "Report",width = 10 ,padx = 5, pady = 5, command = report_window)
report_btn.grid(row=4, column= 1)

#enter button
enter_btn = Button(root, text = "Enter",width = 10 ,padx = 5, pady = 5, command = insert_plan_values )
enter_btn.grid(row=3, column=1)
