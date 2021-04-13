def unique_in_order(iterable):
    # m = []
    # if len(iterable) > 1:
    #     m = [v for i, v in enumerate(iterable) if iterable[i] != iterable[i - 1]]
    #     if len(m) < 1:
    #         m = [iterable[0]]
    # elif len(iterable) == 1:
    #     m = [iterable]
    # return m
    # return [v for i, v in enumerate(iterable) if iterable[i] != iterable[i - 1]] if len(set(iterable)) > 1 else [] if len(iterable) == 0 else [iterable[0]]
    return [v for i, v in enumerate(iterable) if iterable[i] != iterable[i - 1]] if len(
        set(iterable)) > 1 else [] if len(iterable) == 0 else [iterable[0]]

print(unique_in_order('AAA'))