def calculate():
    total = 0
    with open('input.txt', 'r') as file:
        for line in file:
            first_half, second_half = line[:len(line)//2], line[len(line)//2:] 
            s, = set(first_half) & set(second_half)
            if s.islower():
                total += 1 + (ord(s) - ord('a'))
            else:
                total += 27 + (ord(s) - ord('A'))     
    return total

def main():
    print(calculate())

if __name__ == "__main__":
    main()