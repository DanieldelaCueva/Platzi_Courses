divisors = lambda num: [i for i in range(1, num+1) if num % i == 0]

def run():
    try:
        number = int(input("Choose a number "))
        if number < 0:
            raise ValueError()
        print(divisors(number))
    except ValueError:
        print("You must enter a positive number")

if __name__ == "__main__":
    run()