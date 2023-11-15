def calculate(s: str):
    total = 0
    items = iter(s.splitlines())

    while True:
        try:
            s, = set(next(items)) & set(next(items)) & set(next(items))
        except StopIteration:
            break
        else:
            if s.islower():
                total += 1 + (ord(s) - ord('a'))
            else:
                total += 27 + (ord(s) - ord('A'))     
    return total

def read_input():
    input_list = []
    with open('input.txt', 'r') as file:
        for line in file:
            input_list.append(line)

    s = ''.join(input_list)
    return s

def main():
    lines = read_input()
    print(calculate(lines))

if __name__ == "__main__":
    main()