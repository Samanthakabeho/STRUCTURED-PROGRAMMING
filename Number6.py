#slicing the first and last characters
def swap_first_and_last(string):
    first_character = string[0]
    last_character =string[-1]
    
    #swap the first and last characters
    modified_string = last_character + string[1::-1] + first_character
    return modified_string


string ="python"
result = swap_first_and_last(string)
print("result:/")
print("modified string:/")