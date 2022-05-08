accessories_list = {"Stereo System":30.50,"Leather Interior":530.99,"GPS":301.99}
frame_types = {"standard":0,"modified":370.50,"customized":1257.99}
tax_rate = 0.06

#This function checks if the value entered by user
#is a valid number and returns the number in float format 
def validate_allowance(value):
    if not value.strip():
        return 0
    else:
        try:
            value = float(value)
            return value
        except:
            print("input was not valid")
            return -1

# difference between validate_allowance and validate_price
#is that price is not allowed to be empty
def validate_price(value):
    if not value.strip():
        print("Price can not be empty!")
        return -1
    else:
        try:
            value = float(value)
            return value
        except:
            print("input was not valid")
            return -1

#calculates the total cost of accessories
def calculate_accessories(accessories):
    res = 0
    for accessorie in accessories:
        res+=accessories_temp.get(accessorie)
    return res

def calculate_sub_total(price,accesssorie_price):
    return price + accesssorie_price

#calculates the total including tax
def calculate_tax(price,tax_rate):
    return (tax_rate+1)*price

def calculate_total(price_with_tax,allowance):
    return price_with_tax - allowance

#gets the base price, trade-in allowance and accessories from user
def get_user_input():
    while True:
        PRICE = validate_price(input("Enter Base Price: "))
        if PRICE != -1:
            break
    while True:
        ALLOWANCE = validate_allowance(input("Enter Trad-in Allowance: "))
        if ALLOWANCE != -1:
            break
    ACCESSORIES = []
    #asking if each accessorie is needed and if user want to change it's price
    for k,v in accessories_list.items():
        choice = input("Do you want to add {} for extra {}?(y/n) ".format(k,v))
        if choice.lower() == "y":
            choice = input("Do you want to change the price for {}?(y/n) ".format(k))
            if choice.lower() == "y":
                while True:
                    new_price = input("Enter the new price: ")
                    if validate_price(new_price):
                        accessories_temp[k] = float(new_price)
                        break
            ACCESSORIES.append(k)
    return PRICE,ALLOWANCE,ACCESSORIES



accessories_temp = dict(accessories_list)
PRICE = None
ALLOWANCE = None
ACCESSORIES = []

PRICE,ALLOWANCE,ACCESSORIES = get_user_input()

#showing menu
menu_option = input("""Menu:
    C: Calculate
    E: Exit
    R: Reset
    X: Clear
""")

#main loop of program
while True:
    #calculates and displays total
    if menu_option.lower() == 'c':
        accesssories_price = calculate_accessories(ACCESSORIES)
        sub_total = calculate_sub_total(PRICE,accesssories_price)
        total_with_tax = calculate_tax(sub_total,tax_rate)
        print("Subtotal: {:.2f}".format(sub_total))
        print("Subtotal with tax: {:.2f}".format(total_with_tax))
        print("Amount Due: {:.2f}".format(calculate_total(total_with_tax,ALLOWANCE)))
    #exits the program
    elif menu_option.lower() == 'e':
        print("Exiting...")
        break
    #resets the prices for accessories
    elif menu_option.lower() == 'r':
        print("Resetting...")
        accessories_temp = dict(accessories_list)
    #removes the values of base price, trade-in allowance and accessories from users again
    elif menu_option.lower() == 'x':
        PRICE,ALLOWANCE,ACCESSORIES = get_user_input()
    else:
        print("Input is not valid!")
        
    menu_option = input("""Menu:
    C: Calculate
    E: Exit
    R: Reset
    X: Clear
""")
