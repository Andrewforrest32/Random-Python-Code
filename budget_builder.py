def purchase(budget):
    print(list(budget.keys()))
    category = input("Enter the category associated with the purchase: ")
    spent = int(input("Enter the amount spent: "))
    budget[category] -= spent
    return budget
    
def income(budget):
    print(list(budget.keys()))
    multiple = input("Should this income be split between multiple categories (y/n): ")
    money = int(input("Enter the amount made: "))
    if multiple == 'y':
        categories = []
        multiple = int(input("How many categories: "))
        money = money/multiple
        for i in range(multiple):
            category = input("Enter a category associated with the income: ")
            categories.append(category)
        for category in categories:
            budget[category] += money
    elif multiple == 'n':
        category = input("Enter the category associated with the income: ")
        budget[category] += money
    else:
        print("Invalid choice")
    return budget
    
def build_budget(budget):
    while True:
        print(budget)
        category = input("What's the name of the category to be added (or 'stop' when done): ")
        if category == 'stop':
            break
        amount = int(input(f"Enter the amount put aside for {category}:"))
        budget[category] = amount
    return budget
    
def save_budget(budget, filename):
    with open(filename, 'w') as file:
        for category, amount in budget.items():
            file.write(f"{category},{amount}\n")

def load_budget(filename):
    budget = {}
    with open(filename, 'r') as file:
        for line in file:
            category, amount = line.strip().split(',')
            budget[category] = int(amount)
    return budget
    
budget = {}

print("Let's help you make a budget!")
budget = build_budget(budget)
while True:
    print(budget)
    transaction = input("Did you make a 'P'urchase or receive 'I'ncome ('stop' when done):")
    if transaction == 'stop':
        break
    elif transaction == 'P':
        budget = purchase(budget)
    elif transaction == 'I':
        budget = income(budget)
    else:
        print("Invalid choice")