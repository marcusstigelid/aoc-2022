import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def calculate(s: str) -> int:
    n = 0
    for line in s.splitlines():
        ab, cd = line.split(',')
        a_s, b_s = ab.split('-')
        c_s, d_s = cd.split('-')
        a, b = int(a_s), int(b_s)
        c, d = int(c_s), int(d_s)

        if a <= c <= b:
            n += 1
        elif c <= a <= d:
            n += 1
    
    return n

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(calculate(f.read()))

    return 0

if __name__ == "__main__":
    raise SystemExit(main())