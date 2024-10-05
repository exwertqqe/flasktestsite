from flask import Flask, render_template, request, make_response
from config import Config
from forms import site1

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = site1()
    result = None

    # Отримуємо історію з куки
    history_cookie = request.cookies.get('history')
    if history_cookie:
        history = history_cookie.split(';')  # Розділяємо записи за крапкою з комою
    else:
        history = []  # Якщо куки немає, створюємо порожній список

    if form.validate_on_submit():
        expression = form.site.data
        try:
            result = eval(expression)  # Обчислюємо вираз
        except:
            result = 'Error'

        # Додаємо новий запис у форматі "вираз = результат"
        history.append(f"{expression} = {result}")
        history = history[-5:]  # Обмежуємо історію останніми 5 записами

        # Створюємо рядок для збереження в куки
        history_str = ';'.join(history)

        # Створюємо відповідь і зберігаємо оновлену історію в куки
        response = make_response(render_template('site.html', form=form, result=result, history=history))
        response.set_cookie('history', history_str)  # Зберігаємо історію як рядок
        return response

    # Якщо запит GET або не пройшла валідація, повертаємо сторінку з історією
    return render_template('site.html', form=form, result=result, history=history)

if __name__ == '__main__':
    app.run(port=8080)
