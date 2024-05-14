# 1
lst1=list(range(1,51))

lst=[]
# loop
for i in lst1:
    lst.append(i)
print(lst)

# 2
lst2=[]
for num in lst:
    if num%7 ==0 or num%5==0:
        lst2.append(num)
print(lst2)
# 3
total=0
lst3=[]
for i in range(10,41):
    total+=i
    lst3.append(i)
    avg=total/len(lst3)

print(total)
print(avg)

# 4

lst4=[]

# loop
count=0
for i in range(10,50):
    if i%2!=0:
        lst4.append(i)
        if len(lst4)==10:
            break
print(lst4)

# write a program that takes a number as input and 
# prints its multiplication table up to 10 using a for loop.
number=int(input("enter number"))
for i in range(1,11):
    x=i*number
    print(f"{i}* {number} = {x}")

# write a program that counts and prints the number of
#  even numbers between 1 and 50 using a for loop

lst5=[]
for i in range(1,51):
    if i %2==0:
        lst5.append(i)

print(len(lst5))

ls1= [ ("Jay", 20), ("Mo", 30), ("Mya", 32),("qck",50)]
# Display the total quantity of the 3 above
 total_quantity=0

for i in ls1:
    quantity=i[1]
    total_quantity+=quantity

print(total_quantity)

