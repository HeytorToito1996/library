from flask import Flask
from routes.bookRouter import book


app = Flask(__name__)
app.register_blueprint(book)

app.run(debug=True)