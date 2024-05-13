import sqlite3

class bookServices:
    def createBook(self,title,author,genre,quantity,shelf):
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        sql = 'INSERT INTO books(title,author,genre,quantity,shelf) VALUES(?,?,?,?,?)'
        cursor.execute(sql,(title,author,genre,quantity,shelf))
        connection.commit()
        connection.close()
        return 'Livro cadastrado com sucesso'
    
    def updateBook(self, title, author,genre,quantity,shelf,bookId):
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        sqlite = "UPDATE books SET title=?,author=?,genre=?,quantity=?,shelf=? WHERE bookId=?"
        cursor.execute(sqlite,(title,author,genre,quantity,shelf,bookId))
        connection.commit()
        connection.close()
        return 'Livro atualizado com sucesso'
    
    def deleteBook(self,bookId):
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        sqlite = "DELETE FROM books WHERE bookId=?"
        cursor.execute(sqlite,(bookId))
        connection.commit()
        connection.close()
        return 'Livro deletado com sucesso'
    
    def getBooks():
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        sqlite = "SELECT * FROM books"
        cursor.execute(sqlite)
        result = cursor.fetchall()
        connection.close()
        return result
    
    def getBookById(self,id):
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        sql = "SELECT * FROM books WHERE bookId=?"
        cursor.execute(sql,(id,))
        result = cursor.fetchall()
        connection.close()
        return result
    
    def getBookByName(name):
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        sql = "SELECT * FROM books WHERE title=? OR author=? OR shelf=? OR genre=?"
        cursor.execute(sql,(name,))
        result = cursor.fetchall()
        connection.close()
        return result