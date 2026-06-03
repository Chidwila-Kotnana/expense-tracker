import json

try:
   with open("expenses.json","r") as f:
     expense_list = json.load(f)
except FileNotFoundError:
   expense_list = []


def list_of_expenses(to_do):
   
   if to_do =='add':
      
      single_exp_dict = {}
      print("Please provide the amount you've spent:")
      Amount = int(input())
      print("Please provide a relevant category you've spent it for")
      Category = input()  
      single_exp_dict['Amount']=Amount
      single_exp_dict['Category']=Category
      expense_list.append(single_exp_dict)
      with open("expenses.json","w") as f:
            json.dump(expense_list,f)
   else:
      return expense_list


def total_the_amt():
      total=0
      for expense in expense_list:
          total+=expense["Amount"]    
      return total


while True:

     print("Choose one : Add/List/Total/Quit:") 
     to_do = input().lower()

     if to_do == "add":
          list_of_expenses(to_do)
     elif to_do == "list":
          print(list_of_expenses(to_do))
     elif to_do == "total":
          print(total_the_amt())
     elif to_do == "quit":
          break
     else:
          print("Sorry, only these options are supported.\nChoose from: Add/List/Total/Quit.\nBut don't worry, we're developing the application as we talk.")
          

print("Thanks for using this app.")
      
