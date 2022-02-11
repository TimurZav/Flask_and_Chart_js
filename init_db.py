import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

labels = [
    "01/27/2022",
    "01/28/2022",
    "01/29/2022",
    "01/30/2022"
]

values_digits = [
    0.426345357910684,
    0.450576860727911,
    0.430564490221734,
    0.396147378015897,
    0.438111801025979
]

cur = connection.cursor()
for month, digits in zip(labels, values_digits):
    cur.execute("INSERT INTO table_1 (labels, values_digits) VALUES (?, ?)", (month, digits))

# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('FEB', 1190))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('MAR', 1079))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('APR', 1349))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('MAY', 2328))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('JUN', 2504))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('JUL', 2873))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('AUG', 4764))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('SEP', 4349))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('OCT', 6458))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('NOV', 9907))
# cur.execute("INSERT INTO posts (labels, values_digits) VALUES (?, ?)", ('DEC', 16297))

connection.commit()
connection.close()
