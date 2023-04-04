import mysql.connector

class Employees:
    __db = "sfr_users_db"
    __table = "users"

    def __init__(self) -> None:
        self.__connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Qwerty!2345"
        )
        self.__create_database()
        self.__create_table()
    
    def __create_database(self):
        self.__connection.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {self.__db};")
        self.__connection.cursor().execute(f"USE {self.__db}")

    def __create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.__table} (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(16),
            last_name VARCHAR(16),
            login VARCHAR(20) UNIQUE NOT NULL,
            password VARCHAR(20) DEFAULT "qwerty"
        );
        '''
        self.__connection.cursor().execute(query)

    def create_user(self, first, last, login, pswd):
        query1 = f'''INSERT INTO {self.__table} (first_name, last_name, login)
        VALUES ("{first}", "{last}", "{login}");
        '''
        query = f'''INSERT INTO {self.__table} (first_name, last_name, login, password)
        VALUES ("{first}", "{last}", "{login}", "{pswd}");
        '''        
        if len(pswd) < 1:
            self.__connection.cursor().execute(query1)
        else:
            self.__connection.cursor().execute(query)
        self.__connection.commit()
    
    def list_all_users(self):
        query = "SELECT * FROM users;"
        cursor = self.__connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def edit_user(self, id):
        query = f'''UPDATE {self.__table} SET first_name = '{input("Enter first name: ")}',
        last_name = '{input("Enter last name: ")}', login = '{input("Enter login: ")}', password = '{input("Enter password: ")}'
        WHERE id = {str(id)};
        '''
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()

    def search_user(self, name):
        query = f"SELECT * FROM users WHERE first_name = '{name}';"
        cursor = self.__connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.__connection.close()

if __name__ == "__main__":
    emp1 = Employees()
    
    while True:
        u = int(input("""
        1. Create new user
        2. Show all
        3. Edit
        4. Search
        5. Exit
        >>> """))
        
        if u == 1:
            f = input("Enter first name: ")
            l = input("Enter last name: ")
            login = input("Enter login: ")
            pswd = input("Enter password: ")
            emp1.create_user(f.capitalize(), l.capitalize(), login.lower(), pswd.lower())
        elif u == 2:
            res = emp1.list_all_users()
            print(res)
        elif u == 3:
            id = int(input("Enter ID: "))
            emp1.edit_user(id)
        elif u == 4:
            name = input("Enter name: ")
            info = emp1.search_user(name)
            print(f"Id  |   Fullname    |   Login   |   Password\n{info[0][0]}{info[0][1]}{info[0][2]}{info[0][3]}{info[0][4]}")
        elif u == 5:
            break