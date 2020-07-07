def hamming_distance(x: int, y: int) -> int:
    
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]
    
    length = max(len(x_bin), len(y_bin))
    
    x_bin = "0" * (length - len(x_bin)) + x_bin
    y_bin = "0" * (length - len(y_bin)) + y_bin
    
    count = 0
    for i in range(length):
        if x_bin[i] != y_bin[i]:
            count += 1
    
    return count

def main():
    
    x = 1
    y = 4
    
    print(f"{hamming_distance(1, 4)}")
    
    return 0

if __name__ == '__main__':
    exit(main())
