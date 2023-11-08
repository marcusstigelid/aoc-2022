def main():
    numbers = []
    current_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            if line.strip().isnumeric():
                current_list.append(int(line.strip()))
            else:
                numbers.append(current_list)
                current_list = []
        numbers.append(current_list)

    print(top_three_lists_sum(numbers))


def top_three_lists_sum(numbers):
  sorted_numbers = sorted(numbers, key=sum, reverse=True)
  top_three = sorted_numbers[:3]
  top_three_sum = sum(top_three[0]) + sum(top_three[1]) + sum(top_three[2])
  return top_three_sum
    
if __name__ == "__main__":
    main()