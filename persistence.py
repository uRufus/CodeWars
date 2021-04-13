def persistence(n):
    sum_of_digits = 1
    count = 0
    if len(str(n)) > 1:
        for i in str(n):
            sum_of_digits *= int(i)
        count = 1 + persistence(sum_of_digits)
    return count


print(persistence(39)) #3
print(persistence(4)) #0
print(persistence(25)) #2
print(persistence(999)) #4