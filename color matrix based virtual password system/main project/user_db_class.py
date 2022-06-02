import sqlite3
from class_user import user


class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db,check_same_thread=False)
        self.c = self.conn.cursor()
    
    def create_tables(self):
        self.c.execute("""CREATE TABLE users (
                    username varchar(20) primary key not null,
                    password varchar(255)
                    )""")
        self.conn.commit()    


    def add_user(self, user):
        with self.conn:
            self.c.execute("INSERT INTO users VALUES (:username, :password)", 
                {'username': user.username, 'password': user.password})


    def display_search_book(self,username):
        with self.conn:
            self.c.execute("SELECT password FROM users WHERE username = \'"+ str(username).upper()+"\'")
            
        return self.c.fetchall()

    
    def __del__(self):
        self.conn.close()





#book_1 = Book(1, 'abcd', 'xyz', 'pqr', 1000, 10)
#borrower_1 = Borrower('Ashish', 1, 20, '2020-11-19')




#db=Database('store.db')
#book_2 = Book(2, 'abdc', 'zyx', 'rqp', 800, 13)

#book_3 = Book(2, 'abdc', 'zyx', 'rqp', 900, 700)

#db.add_book(book_1)
#db.add_book(book_2)

#books = db.display_book()
#print(books)

#print("--------------------")

#db.update(book_2, 900, 3)
#remove_book(book_1)

#books = db.display_book()
#print(books)






