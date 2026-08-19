from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items')
def items():
    my_books = [
        {"title": "Вивчаємо Python", "author": "Марк Лутц 1 том", "year" : 2022},
        {"title": "Вивчаємо Python", "author": "Марк Лутц 2 том", "year": 2022},
        {"title": "Python легкий довідник", "author": "Пол Беррі", "year": 2023}
    ]
    return render_template('items.html', my_books=my_books)

@app.route('/about')
def about():
    user_info = {
        "name": "Розробник - Женя Снитка",
        "bio": "Мій перший веб-додаток на Flask - думаю і не останній",
        "difficult": "Трохи попарився, але я зміг",
        "coments": "Класне завдання, мені сподобалось"
    }
    return render_template('about.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True)