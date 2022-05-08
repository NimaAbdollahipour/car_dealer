accessories_list = {"Stereo System":30.50,"Leather Interior":530.99,"GPS":301.99}
frame_types = {"standard":0,"modified":370.50,"customized":1257.99}
tax_rate = 0.06

def validate_allowance(value):
    if not value.strip():
        return "0"
    elif value.isnumeric():
        return value
    else:
        print("Input was not valid!")
        return None

def validate_price(value):
    if not value.strip():
        print("Price can not be empty!")
        return None
    elif value.isnumeric():
        return value
    else:
        print("Input was not valid!")
        return None
    
def calculate_accessories(accessories):
    return sum(accessories)

def calculate_tax(price,tax_rate):
    return (tax_rate+1)*price

def calculate_sub_total(price,accesssorie_price):
    return float(price) + accesssorie_price

def calculate_total(price_with_tax,allowance):
    return price_with_tax - float(allowance)

def get_user_input():
    while True:
        PRICE = input("Enter Base Price:")
        if validate_price(PRICE):
            break
    while True:
        ALLOWANCE = input("Enter Trad-in Allowance:")
        if validate_allowance(ALLOWANCE):
            break
    ACCESSORIES = []
    for k,v in accessories_list.items():
        choice = input("Do you want to add {} for extra {}?(y/n)".format(k,v))
        if choice.lower() == "y":
            ACCESSORIES.append(v)
        choice = input("Do you want to change the price for {}?(y/n)".format(k))
        if choice.lower() == "y":
            while True:
                new_price = input("Enter the new price")
                if validate_price(new_price):
                    accessories_temp[k] = new_price
                    break
        ACCESSORIES.append(accessories_temp[k])
    return PRICE,ALLOWANCE,ACCESSORIES


accessories_temp = dict(accessories_list)
PRICE = None
ALLOWANCE = None
ACCESSORIES = []

PRICE,ALLOWANCE,ACCESSORIES = get_user_input()
menu_option = input("""Menu:
    C: Calculate
    E: Exit
    R: Reset
    X: Clear
""")

while True:
    if menu_option.lower() == 'c':
        accesssories_price = calculate_accessories(ACCESSORIES)
        sub_total = calculate_sub_total(PRICE,accesssories_price)
        total_with_tax = calculate_tax(sub_total,tax_rate)
        print("Subtotal:",sub_total)
        print("Subtotal with tax:{:.2f}".format(total_with_tax))
        print("Amount Due:{:.2f}".format(calculate_total(total_with_tax,ALLOWANCE)))
    elif menu_option.lower() == 'e':
        print("Exiting...")
        break
    elif menu_option.lower() == 'r':
        print("Resetting...")
        accessories_temp = dict(accessories_list)
        
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