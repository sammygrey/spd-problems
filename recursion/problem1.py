# Given a sorted array of strings, write a recursive function to find the index of the first
# and last occurrence of a target string.
# If the target string is not found in the array, report that.
# Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
# Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)

first = None
last = None

def recursive_find(arr, item, i=0):
    global first, last

    if i >= len(arr):
        return

    if arr[i] == item:

        if first == None:
            first = i

        elif i+1 < len(arr) and arr[i+1]!=item:
            last = i

        elif i+1 >= len(arr):
            last = i

    i += 1
    recursive_find(arr, item, i)

instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan',
               'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']

recursive_find(instructors, 'Braus')

print(first,last)