import psycopg2
import datetime
import sqlite3

class Database:
     
    def __init__(self):
        # Init database. If you want to use postgresql, just replace the commented code with the declaration below and add values(host,database,user,password)
        try:
            # self.connection = psycopg2.connect(
                # host= "",
                # database="",
                # user="",
                # password=""
            # )
            self.connection = sqlite3.connect('./bored.db')
            
        except psycopg2.Error as e:
            print("Error:", e)
        

        self.cursor = self.connection.cursor()
        # Create table if it not exists
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Bored(activity_id serial PRIMARY KEY,activity VARCHAR (200) NOT NULL,created_on TIMESTAMP NOT NULL )")
        self.connection.commit()
        
    def add(self,activity):
        # Insert activity and timestamp to table 
        creation_date =datetime.datetime.now()
        # self.cursor.execute(f"INSERT INTO bored (activity,created_on) VALUES('{activity}','{creation_date}') ")

        self.cursor.execute("INSERT INTO bored (activity,created_on) VALUES(?, ?) ", (activity,creation_date))
        self.connection.commit()

    def get_value(self):
        # Select values from table
        self.cursor.execute("SELECT activity FROM bored ORDER BY created_on DESC LIMIT 5")
        return self.cursor.fetchall()
    

if __name__ == "__main__":
    db = Database()
    db.get_value()

