import pymysql


def main():
    conn = pymysql.connect(user='fake', password='fake', host='192.168.200.245', port=3306)
    cursor = conn.cursor()
    cursor.execute("select * from mysql.user")
    result = cursor.fetchall()
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
