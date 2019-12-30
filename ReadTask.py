import pymysql
import pandas as pd

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='kirkspockscottyomega289',
    db='belal',
)


try:
    with connection.cursor() as cursor:
        try:
            query = "SELECT * FROM todos"
            cursor.execute(query)
            result = pd.read_sql_query(query, connection)


            print (result)
        except:
            print("Oops! Something wrong")

    connection.commit()
finally:
    connection.close()
