import sqlite3
import pandas as pd
from pandas import DataFrame

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, strr):
    conn.execute(strr)
    conn.commit()

if __name__ == '__main__':
    conn = create_connection('demo.db')
    c = conn.cursor()
    create_table(conn, '''CREATE TABLE STUDENTS([generated_id] INTEGER PRIMARY KEY,[Student_Name] text, [Batch_ID] integer, [Joining_Date] date)''')

    read = pd.read_csv (r'students.csv')
    read.to_sql('STUDENTS', conn, if_exists='append', index = False)

    conn.commit()
    c.execute('''SELECT * FROM STUDENTS''')
    df = DataFrame(c.fetchall(), columns=['Primary_Key','Student_Name','Batch_ID','Joining_Date'])
    print(df)
