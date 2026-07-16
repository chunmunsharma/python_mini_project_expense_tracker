# Expense tracker project
expenses = []  # list of all expenses in form of dictionary.

print("welcome to expense tracker : ")

while True:
    print("\n=====menu=====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")
    
    choice = input("please enter your choice: ")
    
# 1. ADD EXPENSE
    if choice == '1':
        date = input("enter the date on which you spend: ")
        category = input("which type of expense: ")
        description = input("enter additional details: ")
        amount = float(input("enter the amount: "))
        
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("\nDone sir : Expense is added successfully. ")
        
# 2. VIEW ALL EXPENSES
    elif choice == '2':
        if len(expenses) == 0:
            print("no expenses:")
        else:
            print("==== this is all your expense:")
            count = 1
            for eachexpense in expenses:
                print(f" expense no .{count} -> {eachexpense['date']}, {eachexpense['category']}, {eachexpense['description']}, {eachexpense['amount']}")
                count = count + 1
                
# 3. view total spending:
    elif choice == '3':
        total = 0
        for eachexpense in expenses:
            total = total + eachexpense["amount"]
        print("\n TOTAL AMOUNT = ", total)
        
# 4. EXIT
    elif choice == 4:
        print("thankyou for your visit:")
        break
        
    else:
        print("invalid choice")
