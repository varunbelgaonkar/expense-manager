import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root',database='budget')
mycursor = mydb.cursor()

#create_db = "CREATE DATABASE budget"
#mycursor.execute(create_db)

#creating expense table
#query = """CREATE TABLE expense
#    (Date DATE NOT NULL,
#    Amount int not null,
#    description varchar(225),
#    category varchar(225))
#"""
#mycursor.execute(query)


#creating income table
#query = """CREATE TABLE income
#    (Date DATE NOT NULL,
#    Amount int not null,
#    description varchar(225),
#    category varchar(225))
#"""
#mycursor.execute(query)


#creating table to store planned expense
#query = """
#CREATE TABLE plan_expense
#    (date DATE NOT NULL,
#    exp_amount INT,
#    inc_amount INT)
#"""
#mycursor.execute(query)

#creating table to store planned income
#query = """
#CREATE TABLE plan_income
#    (date DATE NOT NULL,
#    amount INT)
#"""
#mycursor.execute(query)


#inserting values in expense table
def exp_values(val):
    query = """INSERT INTO expense(date,amount,description,category)
    VALUES(%s,%s,%s,%s) """
    mycursor.execute(query,val)
    mydb.commit()    


#inserting values in income table
def inc_values(val):
    query = """INSERT INTO income(date, amount, description, category)
    VALUES(%s,%s,%s,%s)"""
    mycursor.execute(query,val)
    mydb.commit()


#inserting values in planned expense
def plan_values(val):
    query = """INSERT INTO plan_expense(date,exp_amount,inc_amount)
    VALUES(%s,%s,%s) """
    mycursor.execute(query,val)
    mydb.commit()

#selecting planned expense value
def plan_exp(month):
    query = f"""
    SELECT exp_amount
    FROM plan_expense 
    WHERE month(date) = {month}
    """
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

#selecting total expense for the month
def total_exp(month):
    query = f"""
    SELECT SUM(amount)
    FROM expense
    WHERE month(date) = {month}
    GROUP BY month(date)
    """
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result


#selecting planned income value
def plan_inc(month):
    query = f"""
    SELECT inc_amount
    FROM plan_expense 
    WHERE month(date) = {month}
    """
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

#selecting total expense for the month
def total_inc(month):
    query = f"""
    SELECT SUM(amount)
    FROM income
    WHERE month(date) = {month}
    GROUP BY month(date)
    """
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result


#selecting expense by categories
def expense_cat(month):
    query = f"""
    SELECT category, sum(amount)
    FROM expense
    WHERE month(date) = {month}
    GROUP by category
    ORDER BY 2
    LIMIT 5
    """
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

#selecting income by categories
def income_cat(month):
    query = f"""
    SELECT category, sum(amount)
    FROM income
    WHERE month(date) = {month}
    GROUP by category
    ORDER BY 2
    LIMIT 5
    """
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result






