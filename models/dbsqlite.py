import sqlite3, os

connection = None

try:
    connection = sqlite3.connect(os.path.abspath('models/kasirr.db'))

except Exception as err:
    print(err)
