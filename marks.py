marks = int(input("Enter marks: "))
# Marks 0 and 100. Above 50 pass, below is fail.
if marks >= 0 and marks <=100:
    if marks > 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Marks")

