import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db_connection()
data_db = conn.execute('SELECT * FROM table_1').fetchall()
data_db_2 = conn.execute('SELECT * FROM table_2').fetchall()
data_db_3 = conn.execute('SELECT * FROM table_3').fetchall()
columns = conn.execute('SELECT * FROM table_1')
columns_2 = conn.execute('SELECT * FROM table_2')
columns_3 = conn.execute('SELECT * FROM table_3')

conn.close()

columns = list(map(lambda x: x[0], columns.description))
columns_2 = list(map(lambda x: x[0], columns_2.description))
columns_3 = list(map(lambda x: x[0], columns_3.description))

colors = ["#23F0E5", "#FF4500"]

labels = [label["labels"] for label in data_db]
values_digits = [value["values_digits"] for value in data_db]

labels_two = [label["labels"] for label in data_db_2]
values_digits_two = [value["values_digits"] for value in data_db_2]

labels_three = [label["labels"] for label in data_db_3]
values_digits_three = [value["Column_1"] for value in data_db_3]
values_digits_two_three = [value["Column_2"] for value in data_db_3]


@app.route('/')
def charts_line_one():
    return render_template('charts.html', title='Table_1', title_2='Table_2',
                           title_3='Table_3', max=17000,
                           labels=labels,
                           values=values_digits, labels_two=labels_two, values_digits_two=values_digits_two,
                           labels_three=labels_three, values_digits_three=values_digits_three,
                           columns=columns[2:], columns_2=columns_2[2:],
                           values_digits_two_three=values_digits_two_three, zip=zip([values_digits_three,
                                                                                     values_digits_two_three],
                                                                                    columns_3[2:], colors))


if __name__ == '__main__':
    app.run()
