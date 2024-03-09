"""📌 Задание №9:
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
📌 Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    context = {'content': 'HomeSTOK'}
    return render_template('main_page.html', **context)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/clothes/')
def clothes():
    context = {'content': 'Линейка стильной одежды'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'content': 'Линейка обуви от Beluccu'}
    return render_template('shoes.html', **context)


@app.route('/clothes/jacket/')
def jacket():
    context = {'content': 'Куртки от ZarA'}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
