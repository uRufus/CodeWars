def digital_root(n):
    while True:
        result = 0
        if len(str(n)) > 1:
            for i in str(n):
                result += int(i)
            n = result
        else:
            return n

    # return n if n < 10 else digital_root(sum(map(int, str(n))))



print(digital_root(976))