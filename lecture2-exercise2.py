'''
  Script that prompts the user for an amount of money and
  # of bills
  Prompt user for bill amounts
  Stop early if balance becomes negative
  Print "All bills paid" if successful
  Print remaining balance at end
'''

def paybills(money, num_bills):
  # Input money and # bills


  # For each bill,
  for i in range(num_bills):
    # Prompt for amount
    bill = float(input(f"Enter bill {i+1} amount: "))
    money -= bill
    if money < 0:
      print('Not enough money')
      # Stop early if overdrawn
      break
  else:
    # Print "All bills paid" if successful
    print('All bills paid')

  # Print final balance
  print('Money:  ', money)

money = float(input('How much money do you have? '))
num_bills = int(input('How many bills to pay? '))
paybills(money, num_bills)
