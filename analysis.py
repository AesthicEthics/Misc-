print("#Usage: An extension to the Timer. Merely type in the subject name you'd like to analyze (ensure correct spelling)")
print("\n")

subject = input("Subject To Analyze: ")

f = open(f'{subject}.txt', 'r')
lines = f.readlines()
times = []
for x in lines: 
    split = x.split("....")
    if len(split) > 1: 
        times.append(split[2])
    else:
        pass
for i in range(len(times)):
    if "\n" in times[i]:
        times[i] = times[i].strip("\n")
        times[i] = times[i].strip(".")
        times[i] = int(times[i])
    else:
        times[i] = times[i].strip(".")
        times[i] = int(times[i])
        pass

total_time = sum(times)

print(f'[+] Total Time Spent On {subject} is {total_time} mins.')

exit_cond = input("Press Enter To Close Program")

if exit_cond == '':
    pass 
