--DROP TABLE IF EXISTS table_1;
--DROP TABLE IF EXISTS table_2;
--DROP TABLE IF EXISTS table_3;

CREATE TABLE if not exists table_1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    labels TEXT NOT NULL,
    values_digits INTEGER NOT NULL
);

CREATE TABLE if not exists table_2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    labels TEXT NOT NULL,
    values_digits INTEGER NOT NULL
);

CREATE TABLE if not exists table_3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    labels TEXT NOT NULL,
    Column_1 INTEGER NOT NULL,
    Column_2 INTEGER NOT NULL
);