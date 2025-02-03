import sqlite3

CONN = sqlite3.connect("db/pet_shop.db")
CURSOR = CONN.cursor()

