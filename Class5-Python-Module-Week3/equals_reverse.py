"""equal_reverse.py
Write a function that controls the given inputs whether they are equal to their reversed order or not."""



def equal_reverse(word):
    if word == word[::-1] : 
        return True
    else : 
        return False
while True : 
    print("for exit press e ")
    word = input("enter word for see reverse is itself  : ")
    if word == "e" or word == "E" :
        break
    else : 
        print(equal_reverse(word))

"""try :  ' ey edip adanada pide ye '"""