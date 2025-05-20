import sqlite3
from datetime import datetime

def initialize_db():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  amount REAL,
                  type TEXT,
                  explanation TEXT,
                  date TEXT)''')
    conn.commit()
    conn.close()

def add_transaction(amount, trans_type, explanation, date):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''INSERT INTO transactions (amount, type, explanation, date)
                 VALUES (?, ?, ?, ?)''',
              (amount, trans_type, explanation, date))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions ORDER BY date DESC')
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_transactions_by_date(date):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions WHERE date = ?', (date,))
    transactions = c.fetchall()
    conn.close()
    return transactions