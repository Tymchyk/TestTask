import psycopg2
import datetime
import sqlite3

class Database:
     
    def __init__(self):
        try:
                # self.connection = psycopg2.connect(
                    # host="127.0.0.1",
                    # database="postgres",
                    # user="postgres",
                    # password="admin"
                # )
                self.connection = sqlite3.connect('./bored.db')

                self.cursor = self.connection.cursor()
                self.cursor.execute("CREATE TABLE IF NOT EXISTS Bored(activity_id serial PRIMARY KEY,activity VARCHAR (200) NOT NULL,created_on TIMESTAMP NOT NULL )")
                self.connection.commit()
        except psycopg2.Error as e:
            print("Error:", e)
        
    def add(self,activity):
        creation_date =datetime.datetime.now()
        # self.cursor.execute(f"INSERT INTO bored (activity,created_on) VALUES('{activity}','{creation_date}') ")

        self.cursor.execute("INSERT INTO bored (activity,created_on) VALUES(?, ?) ", (activity,creation_date))
        self.connection.commit()

    def get_value(self):
        self.cursor.execute("SELECT activity FROM bored ORDER BY created_on DESC LIMIT 5")
        return self.cursor.fetchall()
    

if __name__ == "__main__":
    db = Database()
    db.get_value()

