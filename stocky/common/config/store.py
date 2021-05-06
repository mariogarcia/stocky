import sqlite3
from stocky.common.config import SQLITE_DB_FILE

def create_accounts(db_conn):
    name = db_conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts'")
    if not name:
        db_conn.execute('''create table accounts(id uuid, name text, balance numeric)''')
        print("creating accounts table")
    else:
        print("accounts table already created")


# producer store connection
#store = sqlite3.connect(SQLITE_DB_FILE)

#create_accounts(store)