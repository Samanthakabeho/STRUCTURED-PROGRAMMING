#Removing characters at odd indices
def remove_odd_characters(string):
    modified_string = string[::2]
    return modified_string

#Test the function
string ="computer science"
result = remove_odd_characters(string)
print(f"string:/",{string}/"")
print(f"modified string:/",{result}/"")