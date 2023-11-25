
def calculate(s: str) -> int:
    n = 0
    for line in s.splitlines():
        ab, cd = line.split(',')
        a_s, b_s = ab.split('-')
        c_s, d_s = cd.split('-')
        a, b = int(a_s), int(b_s)
        c, d = int(c_s), int(d_s)

        if a <= c <= d <= b:
            n += 1
        elif c <= a <= b <= d:
            n += 1
    
    return n


def read_input():
    input_list = []
    with open('input.txt', 'r') as file:
        for line in file:
            input_list.append(line)

    s = ''.join(input_list)
    return s

def main():
    foo = read_input()
    print(calculate(foo))

if __name__ == "__main__":
    main()