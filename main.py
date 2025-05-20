import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from database import *

class MoneyManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Manager")
        initialize_db()  # Initialize the database
        
        # Input Fields
        self.amount = tk.DoubleVar()
        self.trans_type = tk.StringVar(value="Add")
        self.explanation = tk.StringVar()
        self.date = tk.StringVar(value=datetime.now().strftime("%d.%m.%Y"))
        
        # Build GUI
        self.create_widgets()
        self.load_transactions()
    
    def create_widgets(self):
        # Entry Fields
        ttk.Label(self.root, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.amount).grid(row=0, column=1)
        
        ttk.Label(self.root, text="Type:").grid(row=1, column=0)
        ttk.Combobox(self.root, textvariable=self.trans_type, values=["Add", "Take"]).grid(row=1, column=1)
        
        ttk.Label(self.root, text="Explanation:").grid(row=2, column=0)
        ttk.Entry(self.root, textvariable=self.explanation).grid(row=2, column=1)
        
        ttk.Label(self.root, text="Date:").grid(row=3, column=0)
        ttk.Entry(self.root, textvariable=self.date).grid(row=3, column=1)
        
        # Buttons
        ttk.Button(self.root, text="Submit", command=self.submit_transaction).grid(row=4, column=0, columnspan=2)
        ttk.Button(self.root, text="View All", command=self.load_transactions).grid(row=5, column=0)
        ttk.Button(self.root, text="Filter by Date", command=self.filter_by_date).grid(row=5, column=1)
        
        # Transaction List
        self.tree = ttk.Treeview(self.root, columns=("ID", "Amount", "Type", "Explanation", "Date"), show="headings")
        self.tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Explanation", text="Explanation")
        self.tree.heading("Date", text="Date")
    
    def submit_transaction(self):
        try:
            add_transaction(
                self.amount.get(),
                self.trans_type.get(),
                self.explanation.get(),
                self.date.get()
            )
            self.load_transactions()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def load_transactions(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for trans in get_all_transactions():
            self.tree.insert("", "end", values=trans)
    
    def filter_by_date(self):
        date = self.date.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for trans in get_transactions_by_date(date):
            self.tree.insert("", "end", values=trans)

if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyManagerApp(root)
    root.mainloop()