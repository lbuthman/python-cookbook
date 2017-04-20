# example tuple
person = ("Luke", "Buthman", 1509, "S. Johnson", "Enid", "OK", 73703, "4052066052", "lbuthman@gmail.com")

# iterate over items, creating variables
first, last, street_number, street, city, state, zip, phone, email = person

# create welcome string with variables
welcome_message = "Hi {0}, do you still live at {1} {2} in {3} {4}?"

# print with passed variables
print(welcome_message.format(first, street_number, street, city, state))

# example array
purchase_info = [12.36, 2, "Power Puff dolls", (2017, 3, 11)]

# iterate over creating variables
price, quantity, item, (year, month, day) = purchase_info

# create purchase transaction string with variables
purchase_details = "Successful transaction on {0}-{1}-{2}. Customer purchased {3} {4} at ${5} each. "

# print with passed variables
print(purchase_details.format(month, day, year, quantity, item, price))

# also works with string or any other iterable data type, can throw away variables easily
when = "now?"

# throw away unwanted letters
n, o, _, _ = when

print("%s%s!" % (n, o))

