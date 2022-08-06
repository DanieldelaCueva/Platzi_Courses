divisors = lambda num: [i for i in range(1, num+1) if num % i == 0]

def run():
        number = input("Choose a number ")
        assert number.isnumeric(), "You must choose a number"
        print(divisors(int(number)))

if __name__ == "__main__":
    run()