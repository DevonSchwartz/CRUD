import pymysql


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='kirkspockscottyomega289',
    db='belal',
)



try:
    with connection.cursor() as cursor:
        number = input("ID to delete: ")
        sql = ("DELETE FROM todos WHERE id = %s")
        try:
            cursor.execute(sql,number)
            print("Successfully Deleted...")
        except:
            print("Oops! Something wrong")

    connection.commit()
finally:
    connection.close()
