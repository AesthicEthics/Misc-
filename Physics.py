
height = (input("Enter Height Values: ").split(","))
velocity = input("Enter Velocity Values: ").split(",")
time = input("Enter Time Values: ").split(",")
n = int(input("How many digits should I round too: "))


mass = 0.08
g = 9.81


def potential(val,r):
    value = mass*g*val 
    value = round(value, r)
    return value 

def kinetic(weight, speed, r):
    value = 0.5*(weight*(speed**2))
    value = round(value, r)
    return value

 

mech = []
pot = []
kin = []

for i in range(len(time)):
    t = float(time[i])
    h = float(height[i])
    v = float(velocity[i])

    pot.append(potential(h,n))
    kin.append(kinetic(mass,v,n))

for i in range(len(kin)):
    mech_val = kin[i] + pot[i]
    mech_val = round(mech_val, n)
    mech.append(mech_val)

for i in range(len(pot)):
    print(f"\n Height: {height[i]} m \n Velocity: {velocity[i]} m/s \n Potential Energy: {pot[i]} J \n Kinetic: {kin[i]} J \n Mechanical: {mech[i]} J\n --------------- \n" )


while True:
    cond = input("Type exit to enter the automater: ")
    
    if cond == "exit":
        break
    else: 
        pass
