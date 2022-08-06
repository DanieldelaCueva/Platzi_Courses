from math import sqrt

def run():
    # my_dict = dict()

    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict.append(i**3)

    return {
        i:i**3 for i in range(1,101) if i % 3 != 0
    }

def test():
    return {
        i:sqrt(i) for i in range(1,1001)
    }

if __name__ == "__main__":
    print(run())
    print(test())