import datetime
my = 0
mm = 0
md = 0
today = str(datetime.datetime.today()).split(" ")[0].split("-")
ty = int(today[0])
tm = int(today[1])
td = int(today[2])
while 1 == 1:
    dob = input("Enter DOB (dd-mm-yyyy): ")
    dmy = dob.split("-")
    if len(dmy) == 3 :
        d = int(dmy[0])
        m = int(dmy[1])
        y = int(dmy[2])
        if (y < 2025) and (m < 13) and (d < 32):
            if not (m == 2 and d > 29):
               my =  ty - y
               mm = tm - m
               if mm < 0:  mm = mm + 12
               md = td - d
               if mm < 0: md = md + 30
               print(f"You are {my} years, {mm} months and {md} days old.")
            else:
                print("Incorrect February has 28/29 days.")
        else:
            print("Incorrect formart use (dd-mm-yyyy)")
    else:
        print("Incorrect formart use (dd-mm-yyyy)")
