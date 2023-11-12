def result_list(input_list):
    results = []
    points = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
                 ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
                 ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7}
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

if __name__ == "__main__":
    main()