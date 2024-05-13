from services.bookServices import bookServices

class bookController:
    def __init__(self) :
        pass

    def getBooks(self):
        return bookServices.getBooks()
    
    def getBookById(self,bookId):
        return self.bookServices.getBookById(self,bookId)
    
    def getBookByName(self,bookName):
        return bookServices.getBookByName(bookName)
    
    def createBook(self,title,author,genre,quantity,shelf):
        return bookServices.createBook(self,title, author, genre, quantity, shelf)
    
    def update(self,title,author,genre,quantity,shelf,bookId):
        return bookServices.updateBook(self,title, author, genre, quantity, shelf,bookId)
    
    def updateBook(self,bookId):
        return bookServices.getBookById(self,bookId)
    
    def deleteBook(self,bookId):
        return bookServices.deleteBook(self,bookId)