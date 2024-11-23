from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

# Инициализация базы данных при запуске приложения
db.create_table()

@app.route('/')
def index():
    """Отображение списка клиентов."""
    clients = db.get_all_clients()
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['GET', 'POST'])
def add_client():
    """Добавление нового клиента."""
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        patronymic = request.form['patronymic']
        birth_date = request.form['birth_date']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']
        db.add_client(first_name, last_name, patronymic, birth_date, check_in_date, check_out_date)
        return redirect('/')
    return render_template('add_client.html')

if __name__ == '__main__':
    app.run(debug=True)
