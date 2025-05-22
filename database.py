import sqlite3
from datetime import datetime

def initialize_db():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  amount REAL,
                  type TEXT,
                  giver TEXT,
                  receiver TEXT,
                  explanation TEXT,
                  date TEXT)''')
    conn.commit()
    conn.close()

def add_transaction(amount, trans_type, giver, receiver, explanation, date):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''INSERT INTO transactions (amount, type, giver, receiver, explanation, date)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (amount, trans_type, giver, receiver, explanation, date))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions ORDER BY date DESC')
    transactions = c.fetchall()
    conn.close()
    return transactions

def delete_transaction_by_id(id):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('DELETE FROM transactions WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# ====================== TOTAL =====================

def get_total_amount_transactions_sum():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM transactions')
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_total_amount_transactions_paid():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM transactions WHERE amount < 0')
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_total_transactions_received():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM transactions WHERE amount > 0')
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_total_received_by_receiver(receiver):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM transactions WHERE receiver = ?', (receiver,))
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_total_sum_by_giver(giver):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM transactions WHERE giver = ?', (giver,))
    transactions = c.fetchall()
    conn.close()
    return transactions

# ======================== TRANSACTIONS =========================

def get_transactions_by_date(date):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions WHERE date = ?', (date,))
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_transactions_by_type(type):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions WHERE type = ?', (type,))
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_transactions_by_giver(giver):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions WHERE giver = ?', (giver,))
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_transactions_by_receiver(receiver):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions WHERE receiver = ?', (receiver,))
    transactions = c.fetchall()
    conn.close()
    return transactions


def get_transaction_checks():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions WHERE  type = ? ORDER BY date DESC', ('Check',))
    transactions = c.fetchall()
    conn.close()
    return transactions

def get_transaction_add_money():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions WHERE amount > 0 ORDER BY date DESC")
    transactions = c.fetchall()
    conn.close()
    return transactions


# ======================= DISTINCT =======================

def get_givers():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT giver FROM transactions WHERE amount > 0')
    receivers = c.fetchall()
    conn.close()
    return receivers

def get_receivers():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT receiver FROM transactions WHERE amount < 0')
    receivers = c.fetchall()
    conn.close()
    return receivers
