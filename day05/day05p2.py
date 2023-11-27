import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def calculate(s: str):
    current_stack, instructions = s.split('\n\n')

    lastline_len = len(current_stack.splitlines()[-1].rstrip())
    stacks: list[list[str]]
    stacks = [[] for _ in range((lastline_len + 2) // 4)]

    for line in current_stack.splitlines():
        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                stacks[i].append(c)

    for stack in stacks:
        stack.reverse()

    for instruction in instructions.splitlines():
        _, number_to_move, _, from_stack, _, destination_stack = instruction.split()
        n, f, d = int(number_to_move), int(from_stack), int(destination_stack)

        last_n_elements = stacks[f - 1][-n:]
        del stacks[f - 1][-n:]

        stacks[d - 1].extend(last_n_elements)

    return ''.join(stack[-1] if stack else '' for stack in stacks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(calculate(f.read()))

    return 0

if __name__ == "__main__":
    raise SystemExit(main())