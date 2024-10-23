#Sum of digits in strings

def sum_of_digits(string):
    total =0
    for character in string:
        if character.isdigit():
            total += int(character)
            return total
        
        string ="Hello 1234"
        result = sum_of-digits(string)
        print(f"sum of digits:{result}")