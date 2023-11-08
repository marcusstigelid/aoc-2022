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

    max_list = max(numbers, key=sum)
    print(sum(max_list))
    
if __name__ == "__main__":
    main()