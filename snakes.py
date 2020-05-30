menu = ["Wings", "Cookies", "Spring Rolls","Salmon", "Steak", "Meat Tornado", "A Literal Garden","Ice Cream", "Cake", "Pie","Coffee", "Tea", "Unicorn Tears"]
x = True

def intro_msg():
  print( """ **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears""" )
intro_msg()
def user_input():
  count = 0
  x = True
  arr = []
  while x == True:
    order = input("""***********************************
    ** What would you like to order? **
    ***********************************: """)
    order1 = str(order)
    arr.append(order1)
    count = arr.count(order1)
    if order1 in menu: 

      print(f"** {count} {order1} of  have been added to your meal **")
   
    if order1 == "q" or order1 == "quit":
      x = False



user_input()
