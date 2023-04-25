'''Counting the frequencies in a list using a dictionary in Python.
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2'''

def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
print(count_frequency(lst))