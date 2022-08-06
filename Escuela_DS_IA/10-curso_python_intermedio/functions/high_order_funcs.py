from functools import reduce

def filtered(my_list):
    return list(filter(lambda x: x % 2 != 0, my_list))

lambda_filtered = lambda my_list: list(filter(lambda x: x % 2 != 0, my_list))

def mapped(my_list):
    return list(map(lambda x: x**2, my_list))

lambda_mapped = lambda my_list: list(map(lambda x: x**2, my_list))

def reduced(my_list):
    return reduce(lambda a,b : a*b, my_list)

lambda_reduced = lambda my_list: reduce(lambda a,b : a*b, my_list)

if __name__ == '__main__':
    print(lambda_filtered([1,4,5,6,9,13,19,21]))
    print(lambda_mapped([1,2,3,4,5]))
    print(lambda_reduced([2,2,2,2,2]))