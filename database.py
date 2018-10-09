import mysql.connector
import sys 
import getopt

global conn,cursor;

conn= mysql.connector.connect(host="localhost",db="database_test")


def connection():
	
	if conn.is_connected():
		print("Connected");
	else:
		print("Not Conected, check ..")

def create_database():
    if connection():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE database_test")
        print("database established")

def create_table():
    conn = mysql.connector.connect(host="localhost", db="database_test")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE rollno(id INT(10) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), dob DATE)")
  


def insert_values():
	cursor = conn.cursor()
	query = "INSERT INTO rollno(id,fname,lname,dob) VALUES (%s,%s,%s,%s)"
	id = input("\nEnter id\n")
	fname = input("\nEnter fname\n")
	lname = input("\nEnter lname\n")
	dob = input("\nEnter dob ( yyyy-mm-dd )\n")
	args= (id, fname, lname, dob);
	cursor.execute(query,args)
	conn.commit()

def alter_table():
   
    cursor = conn.cursor()
    col = input("\nEnter column name\n")
    query = "ALTER TABLE rollno add %s VARCHAR(255)" % (col)
    cursor.execute(query)
    conn.commit()


def truncate_table():
    cursor = conn.cursor()
    query = "DROP TABLE rollno"
    cursor.execute(query)
    conn.commit()

def display():
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rollno")
        rows = cursor.fetchall()
        for x in rows:
            print(x)

def main():
    while True:
        choice = input("Enter the option:")
        if choice == '1':
            create_database()
        if choice == '2':
            create_table()
        if choice == '3':
            insert_values()
        if choice == '4':
            alter_table()    
        if choice == '5':
            truncate_table()
        if choice == '6':
            display()
        if choice == 'q':
            sys.exit()


if __name__ == "__main__":
    main();