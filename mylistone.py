#List is exactly an array. Available methods.
# Type of variable? 
myweek = ["mon","tue","wed","thur","fri","sat","sun"]
myweek.insert(2,"jamuhuri")
myweek.reverse()
myweek.append("holiday")
add_list = ["christmass","Easter","good"]
myweek.extend(add_list)
myweek.remove("mon")
print(myweek)
#Display friday. Index.
print(myweek[2])
#Remove jamuhuri and display weekdays. Slice
myweek.pop(5)
myweek.insert(6,"mon")
print(myweek[2:7])




