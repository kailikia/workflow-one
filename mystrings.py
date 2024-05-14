#Strings - alphanumeric and symbols.
# There are various methods(look like functions) that are used to 
# manipulate strings. Our aim is to learn the various methods
# available in python, index and slicing.

first_name = "    jOHN  "
last_name = "    DOE"

#Clean up and create Full Name
first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
full_name = first_name + " " +last_name

print(full_name)

#Check if it's a email
email = "john@mail.com"
print(email.count("@") == 1)

#Split - It breaks up string according to a criteria
st ="This is my book."

print(type(st.split(" ")))

#Class - Every variable belongs to a certain class.
#Indexing and slicing

