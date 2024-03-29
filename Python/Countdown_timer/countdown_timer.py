import time 
import os
import sys
import subprocess
import winsound


print("\n\n[cyan]Enter the time in whole seconds: [/cyan]")
timer = int(input("> "))


# if the time entered is less than 1, print an error message
while timer < 1:
    print ("[red]Error> [/red] The time Entered is less than 1 second")
    print('\n\n[cyan]Enter the time in whole seconds: [/cyan]')
    timer = int(input("> "))

    # if timer is greater than 60, divit it by 60 and round it to nearest whole number
if timer > 60:
    timer_min = round(timer/60)
    #take the remainder of the timer
    timer_sec = (timer & 60)
    #round timer_sec to nearest whole number
    timer_sec = round(timer_sec)
    
# Create a countdown timer that prints the time every second until the timer reaches 0
def countdown_timer(timer):
    #while loop to run the timer
    while timer > 0:
        #print the timer every second
        print("[cyan]" + str(timer) + "[/cyan]", end=" ".rstrip("\n"),)
        time.sleep(1)
        #decrement the timer by 1
        timer -=1
    print("...", end="".rstrip("\n"))

# Say the to the user that program will exit in "timer" seconds, call the countdown_timer function
if timer > 60:
    print("\n[yellow] The countdown timer will exit in [/yellow]" + str(timer_min) + "[yellow] minutes and [/yellow]" + str(timer_sec) + "[yellow] seconds [/yellow]")
else:
    print("\n[brigh_green]The countdown timer will exit in [/bright_green]"+ str(timer)+"[bright_green] seconds [bright_green]")   
countdown_timer(timer)
print('''[bright_yellow]
 ____                   _
|  _ \  ___  _ __   ___| |
| | | |/ _ \| '_ \ / _ | |
| |_| | (_) | | | |  __|_|
|____/ \___/|_| |_|\___(_)
[/bright_yellow]''')

beep_sound = 10
# If the os is windows play a beep sound using winsound
if os.name == 'nt':
    for i in range(beep_sound):
        winsound.Beep(1000, 500)
        time.sleep(0.1)
else:
    for i in range(beep_sound):
        print("\a")
        time.sleep(0.1)

#In a loop that runs until the user enterts "n", ask the user if they want to run the program again
answer_run_again = "y"

while answer_run_again !="n":
    # Ask the user if they want to run the program again
    print("[brigh_blue]Run again, y/n? [/bright_blue]")
    answer_run_again = input(">> ")
    # if the answer is "y", call the countdown_timer function to run the timer

    if answer_run_again == "y":
        print("\n[cyan] Enter the time in whole seconds: [/cyan]")
        timer = int(input(">> "))
        while timer < 1:
            print("[red]Error: [/red] The time entered is less than 1 second")
            print("\n\n[cyan]Enter the time in whole seconds: [/cyan]")
            timer = int(input(">> "))
        #if timer is greater than 60, divide it by 60 and round it to the nearest whole number
        if timer > 60:
            timer_min = round(timer/60)
            # take the remaind of the timer
            timer_sec = (timer % 60)
            # round timer_sec to the nearest whole number
            timer_sec = round(timer_sec)
        if timer > 60:
            print("\n[yellow]The Countdown timer will exit in [/yellow]" + str(timer_min) + "[yellow] minutes and [/yellow]" + "[yellow] seconds [/yellow]")
        else:
            print("\n[bright_green]The countdown timer will exit in [\bright_green]" + str(timer) + "[bright_green] seconds [/bright_green]")
        countdown_timer(timer)
        print('''[bright_yellow]
         ____                   _
|  _ \  ___  _ __   ___| |
| | | |/ _ \| '_ \ / _ | |
| |_| | (_) | | | |  __|_|
|____/ \___/|_| |_|\___(_)
 
        
        [/bright_yellow]''')
        beep_sound = 10
        # If the os is windows play a beep sound using winsound
        if os.name == 'nt':
            for i in range(beep_sound):
                winsound.Beep(1000,500)
                time.sleep(0.1)
        else:
            for i in range(beep_sound):
                print("\a")
                time.sleep(0.1)
    #Else pass
    else:
        pass
print("\n\n[bright_magenta]Thank you for using the Countdown timer![/bright_magenta]")