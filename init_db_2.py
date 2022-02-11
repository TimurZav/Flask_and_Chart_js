import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

values_digits = [
    0.406589654407637,
    0.391708064299693,
    0.392006520413869,
    0.391747217719396,
    0.400999530864198,
    0.411588452830188,
    0.421763311535636,
    0.449313439710269,
    0.450578969030329,
    0.453238838847385,
    0.459282373099165,
    0.459586630485977,
    0.444619852175769,
    0.436632378297874,
    0.435275835919234,
    0.436958010197578,
    0.432847915816328,
    0.41470582900433,
    0.396751342577031,
    0.408527190850407,
    0.411866697242543,
    0.446925608311983,
    0.413089691809737,
    0.409087837078654

]

cur = connection.cursor()
for month, digits in zip(labels, values_digits):
    cur.execute("INSERT INTO table_2 (labels, values_digits) VALUES (?, ?)", (month, digits))

connection.commit()
connection.close()