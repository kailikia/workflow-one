#Strings - Alphanumeric and symbols. Everything is astring. We 
#intend to learn methods(look like functions) in python that can
#manipulate strings.

#lower() - Lower is a function.
#name.lower() - Lower is method.

first_name = "      JoHN   "
last_name = "DOe   "

#Create full name.Space between the names.
first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
full_name  =  first_name + " " + last_name
print(full_name)

#Email
email = "john@mail.com"
print(email.count("@"))

#Length of characters
print(len(first_name) != 0)

#Split a string using a certain criteria
sent = "This is a laptop."
print(type(sent.split(" ")))

#Indexing and Slicing