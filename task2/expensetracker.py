from expense import Expense

from typing import List
import datetime
import calendar


def main():
    print(f"🎯 Running Expense tracker")
    expense_file_path="./expense.csv"
    
    budget=add_user_income()
    while True:
        print("\n\n1.add expense\n2.view expense\n3.summerize expense\n4.close\n")
        option=int(input("enter option :"))
        switch(option,budget,expense_file_path)
        if option==4:
            break

    

        
   

    
   

def switch(opt,budget,expense_file_path):
    
    #expense_file_path="/Users/ravitejareddybora/Desktop/codingRaja/task-2m/expense.csv"
    if opt == 1:
        exp=get_user_expense()
        save_expense_to_file(exp,expense_file_path)
        return f"Expenditure added"
    
    elif opt == 2:
        return view_expense(expense_file_path)
    elif opt==3:
        return summerize_expense(expense_file_path,budget)
    elif opt==4:
        return clear_expense(expense_file_path)


def clear_expense(expense_file_path):
    
    with open(expense_file_path,'w') as f:
        f.write("")
    print("data cleared")
    
def add_user_income():
    incomes={}
    print(f"🎯 Get_user_income.")
    income_amts=[]
    income_sources=input("Enter Income sources: ").split(',')
    for i in income_sources:
        ia=int(input(f"enter income through {i} :"))
        income_amts.append(ia)
        incomes[i]=ia
    total=0
    print(incomes)
    for i in income_amts:
        total=total+i
    print(f"total income is: {total}")
    return total




def get_user_expense():
    print(f"🎯 Running get_user_expense")
    expense_name=input("Enter Expense name: ")
    expense_amt=float(input("enter expense amount: "))
    expense_categories=[
        "🍱 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc"
    ]
    while True:
        print("Select category : ")
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        value_range=f"[1-{len(expense_categories)}]"
        selected_index=int(input(f"Enter the category number {value_range}: "))-1

        if selected_index in range(len(expense_categories)):
            selected_category=expense_categories[selected_index]
            new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amt)
            return new_expense
        else:
            print("Invalid ctaegory. Please try again!")
        





def save_expense_to_file(expense:Expense,expense_file_path):
    print(f"🎯 Saving expense: {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


    

def summerize_expense(expense_file_path,budget):
    print(f"🎯 summerized expense")
    expenses:list[Expense]=[]
    with open(expense_file_path,"r")as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(",")
            line_expense=Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            #print(line_expense)
            expenses.append(line_expense)
        #print(expenses)

        amount_by_category ={}
        for expense in expenses:
            key=expense.category
            if key in amount_by_category:
                amount_by_category[key]+=expense.amount
            else:
                amount_by_category[key] = expense.amount
    #print(amount_by_category)
    for key,amount in amount_by_category.items():
        print(f"    {key}: rs.{amount:.2f} ")

    total_spent=sum([ex.amount for ex in expenses])
    print(f"You've spent ₹ {total_spent:.2f} this month")

    remaining_budget=budget-total_spent
    print(f"Budget Remaining: ₹ {remaining_budget:.2f}")

    #Get_current_date
    now=datetime.datetime.now()
    days_in_month=calendar.monthrange(now.year,now.month)[1]
    remaining_days=days_in_month-now.day

    daily_budget=remaining_budget/remaining_days

    print(f"budget per day: {daily_budget:.2f}")

def view_expense(expense_file_path):
    with open(expense_file_path,'r')as f:
        lines=f.readlines()
        print('\n')
        if len(lines)==0:
            print ('\n***EMPTY**\n')
        for line in lines:

            print(line)
        
    


if __name__=="__main__":
    main()