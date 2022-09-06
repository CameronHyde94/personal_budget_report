from . import Expense
import matplotlib.pyplot as plt
# Create the BudgetList class and constructor
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

# Define the append method
    def append(self, item):
        if(self.sum_expenses + item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
# Add items to overages that are over budget
        else:
            self.overages.append(item)
            self.sum_overages += item

# Define the __len__() method
    def __len__(self):
        return (len(self.expenses) + len(self.overages))
# Create the __iter__() method
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

# Create the __next__() method
    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()
# Define the main function    
def main():
    myBudgetList = BudgetList(1200)
    # Read in the spending data file
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    # Add the expenses to the BudgetList
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    # Print Length of myBudget List
    print('The count of all expenses: ' + str(len(myBudgetList)))
    
    for entry in myBudgetList:
        print(entry)

    # Create the figure and axes
    fig, ax = plt.subplots()
    # Create the list of labels
    labels = ['Expenses', 'Overages', 'Budget']
    # Create the list of values
    values = [myBudgetList.sum_expenses,
                myBudgetList.sum_overages,
                myBudgetList.budget]
    # Create the bar graph
    ax.bar(labels, values, color=['green', 'red', 'blue'])
    # Set the title
    ax.set_title('Your total expenses vs. total budget')
    # Show the display graph
    plt.show()

if __name__ == "__main__":
    main()

