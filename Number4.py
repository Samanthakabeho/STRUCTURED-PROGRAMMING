#concetrate the two strings

def swap_first_two_characters(string1,string2):
    result =string1+string2
    
    #swap the first two characters
    result =result[1] +result[0] +result[2:]
    return result

#Test the function
string1 ="abc"
string2 ="xyz"
print(f"strings:{string1},{string2}")
print(f"modified string:{swap_first_two_characters(string1,string2)}")

