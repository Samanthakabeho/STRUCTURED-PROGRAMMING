#character of frequency count
def count_character(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
            print(frequency)
string = "samantha"
print("string:",string)
print("character frequency:",count_character(string))
            
    