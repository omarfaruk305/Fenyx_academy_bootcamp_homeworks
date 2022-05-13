""" unique_list.py
Write a function that filters all the unique(unrepeated) elements of a given list."""



def unique_list(x):
    x = set(x)
    x = list(x)
    return x 
print(unique_list([1,1,2,3,4,4,5,5,6,7,8,9,9,9,9,9]))