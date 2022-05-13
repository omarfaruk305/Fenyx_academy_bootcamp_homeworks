""" Write a function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
"""
def reading_number(number):
    """
    12 = 1 is firstdigit , 2 is seconddigit
    """


    firstdigitnumbers = {1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"}
    seconddigitnumbers ={
    2:"twenty-",
    3:"thirty-",
    4:"fourty",
    5:"fifty-",
    6:"sixty-",
    7:"seventy-",
    8:"eighty-",
    9:"ninety-"}
    tenbetweentewenty = {11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifyteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    firstdigitnumber= number % 10 + 0
    seconddigitnumber=number // 10 + 0
    if seconddigitnumber != 0 and firstdigitnumber != 0 :
        if seconddigitnumber == 1  : 
            return tenbetweentewenty[number]
        else : 
            return seconddigitnumbers[seconddigitnumber] + firstdigitnumbers[firstdigitnumber]
    elif firstdigitnumber == 0 and seconddigitnumber !=0 :
        return seconddigitnumbers[seconddigitnumbers]
    elif firstdigitnumber != 0 and seconddigitnumber == 0 : 
        return firstdigitnumbers[firstdigitnumber]

while True : 
    print("press e for exit\nPress only TWO digit")
    number = (input("Number : "))
    if number == "e" or number == "E" : 
        break
    else:
        number = int(number)
        print(f"{number} >>>>>>>>>>>>>>>> {reading_number(number)}")
