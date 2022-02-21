#######################################
########### area_of_Surface&Volume #########
#######################################
# Surface area of a cylinder = 2πr2 + 2πrh.
# Volume of a cylinder = πr2h.
r = int(input("Enter Radius : "))
h = int(input("Enter height: "))
Surface = ((2*3.145*r**2) + (2*3.145*r*h))
Volume = 3.145*r**2*h
print("Surface area of a cylinder is : ",Surface)
print("Volume of a cylinder is : ",Volume)