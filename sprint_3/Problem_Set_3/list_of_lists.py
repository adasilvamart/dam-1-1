usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(univs_data):
    res = [[i for i in univ if type(i) == int] for univ in univs_data]
    total_students = 0
    total_price = 0
    for students, price in res:
        total_students += students
        total_price += price
    return total_students, total_price
        




print(total_enrollment(usa_univs))



#print total_enrollment(usa_univs)
#>>> (77285,3058581079)