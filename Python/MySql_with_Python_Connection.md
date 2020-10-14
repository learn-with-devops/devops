import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="anand@123",
    database="mytest"
)
myc = mydb.cursor()
myc.execute("select * from anand")

data = myc.fetchall()

# # Show databases
# myc.execute("SHOW DATABASES")
# for db in myc:
#     print db

# Create table
# myc.execute("CREATE TABLE anandtest (name varchar(20), branch varchar(10), age int(3))")
# myc.execute("SHOW TABLES")
# for tab in myc:
#     print tab

# Insert Data
# sql = "INSERT INTO anand (name, branch, age) VALUES (%s, %s, %s)"
# val = [("shashikumar", "mech", 24),
#        ("mahesh", "BSC", 27),
#        ("hari", "civil", 26)
#        ]
#
# myc.executemany(sql, val)
#
# mydb.commit()
#
# print (myc.rowcount, "recored inserted")

# Getting Data from DataBase
# for i in data:
#     print ("My name is : ",i[0]," and I belong to ", i[1],".My age is", i[2])

