from flask import Blueprint,render_template,redirect
from flask import request
from controllers.bookController import bookController

book = Blueprint('/books',__name__)
operation = bookController()


@book.route('/books/create', methods=['GET', 'POST'])
def newBook():
    if request.method == 'GET':
        return render_template('books/newBook.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')
        quantity = request.form.get('quantity')
        shelf = request.form.get('shelf')

        # salvar no banco de dados
        try:
             operation.createBook(title, author, genre, quantity, shelf)
             return redirect('/books/getBooks')
        except Exception as error:
            return str(error)


@book.route('/books/getBooks', methods=['GET']) 
def books():
    result = operation.getBooks()
    books = []  # Defina uma lista vazia aqui para evitar UnboundLocalError
    
    if result:
        for book_data in result:
            book_dict = {
                'bookId': book_data[0],
                'title': book_data[1],
                'author': book_data[2],
                'genre': book_data[3],
                'quantity': book_data[4],
                'shelf': book_data[5]
            }
            books.append(book_dict)
    
    return render_template('books/books.html', books=books)



@book.route('/books/search/<name>', methods=['GET'])
def getBookByName(name):
    # Não precisa usar request.form.get() para obter o parâmetro da URL, use name diretamente
    name = request.args.get('name')
    result = operation.getBookByName(name)
    books = []  # Defina uma lista vazia aqui para evitar UnboundLocalError
    
    if result:
        for book_data in result:
            book_dict = {
                'bookId': book_data[0],
                'title': book_data[1],
                'author': book_data[2],
                'genre': book_data[3],
                'quantity': book_data[4],
                'shelf': book_data[5]
            }
            books.append(book_dict)
    
    return render_template('books/bookSearch.html', books=books)

@book.route('/books/update/<bookId>',methods=['GET','POST'])
def updateBook(bookId):
    result = operation.updateBook(bookId)
    if request.method == 'GET':
        if result:
            book = result[0]
            
            bookDict = {
                'bookId': book[0],
                'title': book[1],
                'author': book[2],
                'genre': book[3],
                'quantity': book[4],
                'shelf': book[5]
            }
        return render_template('books/updateBook.html', book=bookDict)
    elif request.method == 'POST':
        bookId = bookId
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')
        quantity = request.form.get('quantity')
        shelf =  request.form.get('shelf')
        
        #salvar no banco de dados
        try:
            operation.update(title=title, author=author, genre=genre, quantity=quantity, shelf=shelf,bookId=bookId)
            return redirect('/books/getBooks')
        except Exception as error:
            return str(error)
        
        
@book.route('/books/delete/<bookId>',methods=['GET'])
def deleteBook(bookId):
    bookId = bookId
    try:
        operation.deleteBook(bookId)
        return redirect('/books/getBooks')
    except Exception as error:
        return str(error)