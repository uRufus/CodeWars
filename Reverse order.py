def descending_order(num):
    # Bust a move right here
    # new_list = [int(i) for i in str(num)]
    # new_list.sort(reverse=True)
    # return int("".join(map(str, new_list)))
    return int("".join(sorted(str(num), reverse=True)))



print(descending_order(0))
print(descending_order(15))
