""" 
-- Task: Repeating an action multiple times is what computers are really good at! --
Write a program that always asks the user to enter a number.
When the user enters the negative number -1, the program should
stop requesting the user to enter a number. The program must then
calculate the average of the numbers entered excluding the -1. 
"""

user_input_list = []
min_number = 0

while True:
    try:
        num = int(input("Input an integer: "))
    except ValueError:
        num = int(input("Input an integer: "))

    user_input_list.append(num)
    if num <= min_number:
        break

user_input_list.pop()
average = sum(user_input_list) / (len(user_input_list))
print(f'Average of yours numbers {average}')
