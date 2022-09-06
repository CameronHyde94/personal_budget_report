from . import Expense
import collections
import matplotlib.pyplot as plt

"""Create a variable named expenses and set it equal 
to calling the Expense.Expenses() constructor. Then 
call the read_expenses() method on expenses and pass 
in the name of the file data/spending_data.csv."""
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

"""Create an empty list called spending_categories."""
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

"""Counter Categories with a Counter Collection"""
spending_counter = collections.Counter(spending_categories)
print(spending_counter)

"""Get the Top 5 Categories"""
top5 = spending_counter.most_common(5)

"""Convert the Dictionary to 2 Lists"""
categories, count = zip(*top5)

"""Plot the Top 5 Most Common Categories"""
fig, ax = plt.subplots()

"""Create the bar chart"""
ax.bar(categories, count)

"""Add a title"""
ax.set_title('# of Purchases by Category')

"""Display the graph"""
plt.show()