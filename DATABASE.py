import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="SV"
)
c = conn.cursor()

Trip_Creation = "create table SV(TripName varchar(50), Name varchar(50), Amount int not null ,Total int not null ,remark varchar(50))"
c.execute(Trip_Creation)

conn.commit()
c.close()
conn.close()


