def find_it(seq):
    # odd = [number for number in set(seq) if seq.count(number) % 2 != 0]
    # return odd[0]
    return [number for number in set(seq) if seq.count(number) % 2 != 0][0]


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


def tickets(people):
    cash = 0
    for i in people:
        if i == 25:
            cash += 25
        elif i - 25 <= cash:
            cash = cash - i + 25
        else:
            return "NO"
    return "YES"


print(tickets([25, 25, 25, 75, 50]))
print(tickets([25, 25, 50, 100]))
print(tickets([100]))


def count(string):
    # counter = {}
    # for i in string:
    #     if i not in counter:
    #         counter[i] = 1
    #     else:
    #         counter[i] += 1
    # return counter
    return {v: string.count(v) for v in set(string)}


print(count('abade'))


