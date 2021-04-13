def open_or_senior(data):
    return ["Senior" if i[0] > 54 and i[1] > 7 else "Open" for i in data]



print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))