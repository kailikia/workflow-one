num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))
large = 0
pos = 0
if num1 > num2 and num1 > num3:
    large = num1
    pos =1
elif num2 > num1 and num2 > num3:
    large = num2
    pos =2
elif num3 > num1 and num3 > num2:
    large = num3
    pos =3
else:
    print("All numbers are Equal")
print(f"Num {pos} with value {large} is largest.")