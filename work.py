height_pairs = (input("Enter Height Pair Value, seperate pairs by spaces (hi, hf)): ").split(" "))
velocity_pairs = (input("Enter Height Pair Value, seperate pairs by spaces, (vi, vf)): ").split(" "))
n = int(input("How Many Digits Should I Round To: "))

m = 0.08 
g = 9.81

delta_y = []
delta_ek =[]

for i in range(len(height_pairs)):
    main_val = height_pairs[i].split(',')
    difference = float(main_val[1]) - float(main_val[0])
    delta_y.append(difference)


for i in range(len(velocity_pairs)):
    main_val = velocity_pairs[i].split(',')
    kf = 0.5*m*((float(main_val[1]))**2) 
    ki = 0.5*m*((float(main_val[0]))**2) 

    diff = round((kf - ki), n) 
    delta_ek.append(diff) 
    




for i in range(len(delta_y)):
    value = -m*g*delta_y[i]
    value = round(value, n)
    print(f" Height Pair: {height_pairs[i]}\n Work Done: {value} J\n Delta Y: {round(-delta_y[i],n)}\n Delta-Ek: {delta_ek[i]} J\n -------------\n")


while True:
    cond = input("Type exit to enter the automater: ")

    if cond == "exit":
        break
    else: 
        pass
