def run():
    set1 = {1, 5, "Hello", 12.4, True, (4,2)}

    set2 = {4.2, "World", 7, True, 1}

    full_join = set1 | set2

    inner_join = set1 & set2

    outer_join = set1 ^ set2

    left_join = set1 - set2

    right_join = set2 - set1

    print(f"Set 1: {set1} | Set 2: {set2}")
    print(f"Full join: {full_join}")
    print(f"Inner join: {inner_join}")
    print(f"Outer join: {outer_join}")
    print(f"Left join: {left_join}")
    print(f"Right join: {right_join}")

if __name__ == "__main__":
    run()