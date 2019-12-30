import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='kirkspockscottyomega289',
    db='belal',
)



try:
    with connection.cursor() as cursor:
        title = input("Change title: ")
        desc = input("Change desc: ")
        number = input ("What ID Do You Want to Update?: ")
        sql = "UPDATE todos SET `title`=%s, `desc`=%s WHERE `id` = %s"
        try:
            cursor.execute(sql,(title,desc,number))
            print("Successfully Updated...")
        except:
            print("Oops! Something wrong")

    connection.commit()
finally:
    connection.close()
