def check(list):
    for not_sorted_list in list:
        sorted_list = sorted(not_sorted_list)
        a = ''.join(sorted_list)
        print(sorted_list)
        if a == list[0]:
            print("The lists are the same")
        else:
            print("The lists are not the same")

check_lists = check(['abcd','bacd','dbac'])
print(check_lists)
