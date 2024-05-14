#  function to calculate the area of a triangle
# def area_triangle():
#     base=20
#     height=30
#     area=(base*height)*0.5
#     print(area)

# area_triangle()

# write a function to calculate the area square

def area_square():
    a=6
    area=a**2
    print(area)

area_square()

# parameters and arguments
#  function to calculate the area of a triangle
def area_trangle(a,b):
    area=(a*b)*0.5
    print(area)

area_trangle(10,20)
area_trangle(30,20)

# write a function to calculate the area square (use parameters and arguments)
def area_square(a):
    area = a**2
    print(area)

area_square(4)
# Return the result of a function
def return_area_square(a):
    area=a**2
    return area
b=return_area_square(5)
print(b)

def return_volume_cuboid(area,height):
    volume= area*height
    return volume
v=return_volume_cuboid(b,10)
print(v)