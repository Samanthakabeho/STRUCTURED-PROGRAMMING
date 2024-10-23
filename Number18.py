# Counting character types
def count_character_types(string):
    uppercase = 0
    lowercase =0
    special_characters =0
    numeric_values =0
    
    for character in string:
        if character.isupper():
            uppercase +=1
        elif character.islower():
            lowercase +=1
        elif character.isdigit():
            numeric_values +=1
        else:
            special_characters +=1
            
            print("uppercase:",uppercase)
            print("lowercase:",lowercase)
            print("special characters:")
            print("numeric_values:",numeric_values)