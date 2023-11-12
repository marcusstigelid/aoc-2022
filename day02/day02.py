def result_list(input_list):
    results = []
    points = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3,
                 ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
                 ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}
    for tup in input_list:
        if tup in points:
            results.append(points[tup])
    return results
    

def read_input():
    input_list = []
    with open('input.txt', 'r') as file:
        for line in file:
            tup = tuple(line.split())
            input_list.append(tup)
    return input_list


def main():
    tuples_list = read_input()
    sum_list = result_list(tuples_list)
    print(sum(sum_list))

# A/X Rock, B/Y Paper, C/Z Scissors
# 1 point for rock, 2 for paper, 3 scissors
# 0 point for loss, 3 draw, 6 win
# (A, X) = 4, (A, Y) = 8, (A, Z) = 3
# (B, X) = 1, (B, Y) = 5, (B, Z) = 9
# (C, X) = 7, (C, Y) = 2, (C, Z) = 6

if __name__ == "__main__":
    main()