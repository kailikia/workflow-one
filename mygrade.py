#Return pass > 50, else fail. Marks 0 and 100
marks = int(input("Enter marks: "))
if marks >= 0 and marks <= 100:
    # Check if A,B,C,D,E
    if marks >= 50:
        print("pass")
    else:
        print("fail")
else:
    print("Invalid marks") #Task on slide53

