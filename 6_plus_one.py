def plus_one(digits: list) -> list:
    
    number = int("".join([str(i) for i in digits]))
    
    number += 1
    
    digits = [int(i) for i in str(number)]
    
    return digits

def main():
    
    digits = [1, 2, 3]
    
    print(f"{plus_one(digits)}")
    
    return 0

if __name__ == '__main__':
    exit(main())
