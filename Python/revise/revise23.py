# 21.  Write a Python program to check if a list is empty or not. 


def is_list_empty(lst):

    return len(lst) == 0


lst = []

print(f"Is the list empty? {'Yes' if is_list_empty(lst) else 'No'}")
