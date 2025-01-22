# データベースからデータをとってくる
import mysql.connector
def mysqlconnector():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="8VBJtMueZY#w", database="dog"
    )

    if conn.is_connected():
        print("MySQLへの接続が完了しました")

    cursor = conn.cursor()

    cursor.execute("SELECT dog_name FROM dog_list")

    rows = cursor.fetchall()

    print("テーブルデータ")
    dog_name_list = [row[0] for row in rows]  # fetchallはタプル型で返ってくるので
    print(dog_name_list)
    cursor.close()
    conn.close()
    return dog_name_list