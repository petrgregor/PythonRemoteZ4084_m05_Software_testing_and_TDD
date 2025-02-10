def _get_data(how_much):
    with open('test2.txt', 'r') as f:
        return f.read(how_much)


def get_avg(how_much):
    data = _get_data(how_much)
    #print(f"data: {data}")
    numbers = [int(x) for x in data]
    #print(f"numbers: {numbers}")
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    #print(get_avg(5))

    for how_much in range(1, 10):
        #r = ''.join(str(i) for i in range(1, how_much+1))
        r = ''
        for i in range(1, how_much+1):
            r += str(i)
        print(f"{how_much} -> {r}")
