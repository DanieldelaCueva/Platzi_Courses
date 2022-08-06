def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("Empty string")
        else:
            return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
    

if __name__ == "__main__":
    try:
        print(palindrome(""))
    except TypeError:
        print("You can only enter strings")
    