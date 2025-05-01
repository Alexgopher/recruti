import pandas as pd
import mysql.connector
config = {
    'host': '*.beget.tech',
    'user': '*_recruti',
    'password': 'r3Cr7t1',
    'database': '*_recruti',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

sql = "SELECT * FROM linkedin_profiles"

cursor.execute(sql)
res = cursor.fetchall()
print(res)
cnx.commit()
cursor.close()
cnx.close()

