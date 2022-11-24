grocery_cart =[]
new_grocery_cart = []

def enter_p():
    x = input("Enter a grocery ")
    return x

def add_p(p):
    y = enter_p()
    p.append(y)

add_p(grocery_cart)


def display_p():
    print(f"The groceries are: {grocery_cart}")


def add_another_p(arg):
    x = 0
    while x < len(grocery_cart): 
        z = input("Enter Y to add another  or N to exit ")
        if z == 'Y':
            add_p(grocery_cart)
        elif z =="N":
            display_p()
            break
        else:
            print("Invaild input")
            add_another_p(arg)
        
    
        
    
add_another_p(grocery_cart)
#add_p(grocery_cart)


def to_lower_case():
    x = 0
    while x < len(grocery_cart):
        y = grocery_cart[x].lower()
        new_grocery_cart.append(y)
        x = x + 1

to_lower_case()
# print(new_grocery_cart)


def search_grocery_cart():
    x = input("Search for a grocery")
    y = x.lower()
    z = 0
    if y in new_grocery_cart[z]:
        count_item = new_grocery_cart.count(y)
        total = len(new_grocery_cart)
        print("Number of", y, "is: ", count_item)
        print("Total item in grocery is: ", total)
    else:
        print("Item not found")
    
search_grocery_cart()





