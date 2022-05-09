import math
def free_body(angle_arr): 
    mass = 0.005
    g = 9.81
    FT_x = []
    for i in range(len(angle_arr)):
        FT = (mass*g*(math.tan(math.radians(float(angle_arr[i])))))
        FT = round(FT, 4)
        FT_x.append(FT)
    return FT_x 
def colombs(distance_arr):
    k = (8.99*(10**9))
    q = (8.00*(10**-9))
    mains = []
    for i in range(len(distance_arr)):
        value = (k*(q**2))/((float(distance_arr[i])/100)**2)
        value = round(value, 4)
        mains.append(value)
    return mains
forces = input('Enter Angle Array Here: ').split(',')
dist = input('Enter Distance Array Here: ').split(',')
proven = free_body(forces)
check = colombs(dist)
for i in range(len(forces)):
    difference = round(100-((proven[i]/check[i])*100), 2)
    mass = 0.005
    g = 9.81
    FG = round(mass*g,4)
    FT = round(math.sqrt(proven[i]**2 + ((FG))**2),4)
    print(f'Angle: {forces[i]} | Distance: {dist[i]} | Forces Value: {(proven[i])}  | Colomb Value: {check[i]} | Difference: {difference}% | Tension: {FT} | Gravity: {FG}')
