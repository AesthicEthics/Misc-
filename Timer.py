import time 
import datetime 

while True: 
    print("#Usage: You can type in any subject and program will create a file for it in the same directory as the program")
    print("#Usage: Be sure to check the spelling of the subject. A difference in spelling may lead to your progress being written in another file")
    print("#Usage: To exit the program, you can Ctrl+C or leave the Subject Field Empty followed by [n] in the Start Timer Field")
    print('\n')
    print("@luscious @AesthicEthics")
    print("\n")

    subject = input('Subject: ')
    start_cond = input("Would you like to start the timer.... [y] or [n]: ")

    if start_cond == 'y':
        start = time.time()

        while True: 
            exit_cond = input("Press Enter to stop timing or type 'time' to check the time invested so far: ")

            if exit_cond == "":
                end = time.time()
                total_time = round(((end) - (start))/60)
                print("[+] Timer stopped")
                print("[+] Logging Entry")
                f = open(f'{subject}.txt','a+')
                f.write("\n")
                f.write(f" {datetime.datetime.now()}..... {subject}.....{total_time}")
                f.close()
                print("[+] Entry Logged")
                break 
            elif exit_cond == "time":
                end = time.time()
                total_time = round(((end) - (start))/60)
                print(total_time)
        
    elif start_cond == "n":
        break 
