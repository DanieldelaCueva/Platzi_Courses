def run():
    # squares = []
    # for i in range(1, 101):
    #     if i%3 != 0:
    #         squares.append(i**2)

    return [i**2 for i in range(1,101) if i%3!=0]

def test():
    return [i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]


if __name__ == "__main__":
    print(run())
    print(test())