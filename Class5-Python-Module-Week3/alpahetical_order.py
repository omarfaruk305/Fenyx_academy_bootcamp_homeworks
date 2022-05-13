""" alphabetical_order.py
Write a function that takes an input of different words with hyphen (-) in between them and then:

sorts the words in alphabetical order,
adds hyphen icon (-) between them,
gives the output of the sorted words. """

def alphabetical_order (words):
    wordlist=words.split("-") 
    wordlist.sort()
    sortedwords = ""
    for i in wordlist : 
        sortedwords = sortedwords+ "-" +i
    sortedwords = sortedwords.strip("-")
    return sortedwords
words = input("Enter words with hyphen (-) : ")
print(alphabetical_order(words))