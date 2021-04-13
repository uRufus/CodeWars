# def dirReduc(arr):
#     guide2 = arr[0]
#     # directions = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
#     # # guide = {v.upper(): arr.count(v) for v in set(arr)}
#     # # for i, v in directions.items():
#     # #     if guide[i] > guide[v]:
#     # #         for b in range(guide[i] - guide[v]):
#     # #             guide2.append(i)
#     # # return guide2
#     # for i in range(1, len(arr) - 1):
#     #     if directions[i - 1] == arr[i]:
#
#
#     return guide2
#
# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# print(dirReduc(a))


def wave(people):
    # return [people.replace(people[i], people[i].upper(), 1) for i in range(0, len(people))]
    return [people[:i].lower() + people[i].upper() + people[i + 1:].lower() for i in range(0, len(people)) if people[i]
            != " "]

print(wave(" Two words"))