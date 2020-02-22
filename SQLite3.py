# Integrating SQLite 3 with Python using sqlite3 module

import sqlite3
cnnect = sqlite3.connect('test.db')
print("Database opened")
cnnect.execute("CREATE TABLE (ID INT PRIMARY KEY  NOT NULL,

            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50));")
print("Table created")

cnnect.close()            
