# dog_list.txtからmysqlに登録するファイル
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="8VBJtMueZY#w", database="dog"
)

if conn.is_connected:
    print("データベースに接続しました")

cursor = conn.cursor()
cursor.execute("TRUNCATE TABLE dog_list")
conn.commit()
with open("dog_list.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()  # データベースを整理するため
        cursor.execute(f"insert into dog_list (dog_name) values ('{line}')")
        conn.commit()

cursor.close()
conn.close()
