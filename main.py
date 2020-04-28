import mysql.connector
from faker import Faker
import csv

db = mysql.connector.connect(
    host="34.82.239.1",
    user="root",
    passwd="grocery408",
    database="finalproject_pantry2",
)

fake = Faker()

def printDatabase():
    print("printing current data in the database...")
    mycursor = db.cursor()

    print("______________Pantry________________")
    mycursor.execute("SELECT * FROM Pantry")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("______________Prices________________")
    mycursor.execute("SELECT * FROM Prices")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("______________Purchase Date________________")
    mycursor.execute("SELECT * FROM PurchaseDate")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("______________Net weight of items in grams________________")
    mycursor.execute("SELECT * FROM Weight")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("______________Food groups & Description________________")
    mycursor.execute("SELECT * FROM FoodGroups")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    db.close();

#def createCSV(file, tuple):
    #with open(file, tuple) as csvfile:

choice = input("to generate data in a csv file, press 'g'. To print the current database press 'p' ")
if choice == 'g':
    fileName = input("enter a file name you want to save the file as, in the format 'name.csv' ")
    numTuple = input("enter how many tuples you want generated")
    print("generating csv file...")
    #createCSV(fileName, numTuple)

elif choice == 'p':
    printDatabase()










