from typing import Tuple, Any

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="SV"
)
c = conn.cursor()

def Name(title,n):
    i = 0
    if n < 2:
        print("Can not work for one person")
    else:
        while i < n:
            name = input("Enter name of the person: ")
            query = "INSERT INTO SV (TripName, Name, Amount, Total) VALUES(%s, %s, 0, 0)"
            c.execute(query,(title,name))
            i += 1
        conn.commit()
        print("The names have been added.")

def S_amount(name,n):
    Option=input("1) Add\n2) Remove")
    if Option=='Add' or 1:
        particular_name = name
        T_amount = int(input("Enter the total amount: "))
        splitted_amount = T_amount / n
        query_amount=f"update SV set Amount=Amount+{splitted_amount}, Total=Total+{T_amount} where TripName = '{particular_name}'"
        c.execute(query_amount)
        conn.commit()
        print("Amount added successfully")
    elif Option=='Remove' or 2:
        particular_name = name
        T_amount = int(input("Enter the total amount: "))
        splitted_amount = T_amount / n
        query_amount = f"update SV set Amount=Amount-{splitted_amount}, Total=Total-{T_amount} where TripName = '{particular_name}'"
        c.execute(query_amount)
        conn.commit()
        print("Amount removed successfully")
    else:
        print("Invalid Option")

def view():
    Trip_name=str(input("Enter Name of particular you want to view: "))
    check_view_query = f""" SELECT COUNT(*) AS view_count FROM information_schema.views WHERE table_schema = 'SV' AND table_name = '{Trip_name}';"""
    c.execute(check_view_query)
    view_exists = c.fetchone()[0]
    print(view_exists)
    if view_exists==0:
        query_view=f"CREATE VIEW {Trip_name} AS SELECT TripName, Name, Amount FROM SV WHERE TripName='{Trip_name}';"
        c.execute(query_view)
        conn.commit()
        show_view=f"select * from {Trip_name}"
        c.execute(show_view)
        result_view = c.fetchall()
        for r in result_view:
            print(r)
    else:
        show_view = f"select * from {Trip_name}"
        c.execute(show_view)
        result_view = c.fetchall()
        for r in result_view:
            print(r)
    conn.commit()


print("Welcome to SV. \n \t Please select the option you want to use.")
def code():
    while (True):
        global n
        print("""1)New Particular
2)Amount
3)View
4)Exit\n""")
        choice = int(input(""))

        if choice==1:
            title = input("Enter Title: ")
            n = int(input("Enter number of persons (at least more than 2): "))
            print(Name(title,n))


        elif choice==2:
            particular_name=input("Enter name of the particular: ")
            check_query=f"SELECT COUNT(*) AS name_count FROM SV WHERE TripName = '{particular_name}';"
            c.execute(check_query)
            result = c.fetchone()
            name_count = result[0]
            if name_count == 0:
                print("No particular exist.")
            else:
                print(S_amount(particular_name,name_count))


        elif choice==3:
            print(view())
        elif choice==4:
            print("Thank you!!")
            break
        else:
            print("Invalid Choice, Try again")
print(code())
conn.commit()
c.close()
conn.close()

