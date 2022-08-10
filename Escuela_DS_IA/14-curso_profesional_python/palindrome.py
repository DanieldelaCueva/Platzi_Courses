from math import sqrt

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def is_prime(n: int) -> bool:
    for i in range(2, round(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(7))
