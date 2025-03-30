import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="SV"
)
c = conn.cursor()
# s="suyash"
#NotNull="ALTER TABLE trip Modify Amount int NOT NULL"
#NotNull1="ALTER TABLE trip Modify Total int NOT NULL"
#c.execute(NotNull1)
Trip_Creation = "create table SV(TripName varchar(50), Name varchar(50), Amount int not null ,Total int not null ,remark varchar(50))"
c.execute(Trip_Creation)
# Amount_Table="create table Amount(TripName varchar(50),Amount int)"
# c.execute(Amount_Table)
conn.commit()
c.close()
conn.close()


