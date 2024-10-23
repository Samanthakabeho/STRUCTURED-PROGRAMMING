#Split the string into a list
def reverse_words(string):
    words =string.split()
    reversed_words =''.join(reversed(words))
    return reversed_words


string = "hello world"

print("string:",string)

print("reversed words:",reverse_words(string))

    