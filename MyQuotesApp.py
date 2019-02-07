import tkinter as tk
import sqlite3
import random

#colors list for bg
colors = ['lightgreen','lightblue','lightyellow']

def random_item(list):
	return (random.choice(list))

def random_quote():
	return (random.randrange(1,283))

#db connect, add new quotes and select one qoute from db
conn = sqlite3.connect('baza.db')
c = conn.cursor()

random_quote_id = random_quote()

#fetching quote from db
c.execute("SELECT * FROM Citati WHERE id=?",(random_quote_id,))
quotes = c.fetchall()

#new just_quotes list that will have just quotes without id
chosen_quotes = []

for item in quotes:
	chosen_quotes.append(item[1])
c.close()

#random color and quote choices
color = random_item(colors)
quote = random_item(chosen_quotes)

#core tk config
root = tk.Tk()
msg = tk.Message(root, text=quote)
msg.config(bg=color, font=("times",26,"italic"))
msg.pack()

tk.mainloop()