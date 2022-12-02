""" 
-- Task: Checking whether a statement is true or false allows the code to make intelligent decisions  --
At your school, the front gate is locked at night for safety. 
You often need to study late on campus. There is sometimes a 
night guard on duty who can let you in. You want to be able 
to check if you can access the school campus at a particular time.

The current hour of the day is given in the range 0, 1, 2 … 23 and 
the guard’s presence is indicated by with a True/False boolean.

If the hour is from 7 to 17, you do not need the guard to be there as the gate is open
If the hour is before 7 or after 17, the guard must be there to let you in

Example start:
hour = 4
guard = True

Example output:
'You're in!'
"""

def go_to_study(user_hour):
    gates_open = list(range(7, 18))
    if user_hour in gates_open:
        print("You're in!")
    else:
        guard = input("Your with guard?:")
        if user_hour not in gates_open and guard == 'True':
            print("You're in!")
        else:
            print("You need guard to enter!")


user_hour = int(input("Hour:"))
go_to_study(user_hour)
