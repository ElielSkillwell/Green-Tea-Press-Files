def grid(size):
    plus_string = f'+ {"- " * size}+ {"- " * size}+'
    middle_string = f'| {"  " * size}| {"  " * size}|'
    for i in range((size + 1) * 2 + 1):
        if i % (size + 1) == 0:
            print(plus_string)
            continue
        print(middle_string)


grid(5)
