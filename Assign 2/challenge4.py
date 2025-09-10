import mysql.connector

if __name__ == '__main__':
    # Connect to server
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="605166")
    
    print(mydb)

    # Get a cursor
    cur = mydb.cursor()

    # CREATE DATABASE
    # cur.execute("CREATE DATABASE IF NOT EXISTS librarydb")
    
    # USE DATABASE
    # cur.execute("USE librarydb")
    
    # CREATE TABLE book
    # cur.execute("""
    #         CREATE TABLE book (
    #             id INT AUTO_INCREMENT PRIMARY KEY,
    #             title VARCHAR(255) NOT NULL,
    #             author VARCHAR(255) NOT NULL,
    #             isbn VARCHAR(20) NOT NULL,
    #             file_format VARCHAR(20)
    #         )
    #     """)
    
    cur.execute("SELECT * FROM book")


    # Close connection
    mydb.close()