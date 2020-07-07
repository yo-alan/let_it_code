def arrangeCoins(n: int) -> int:
    
    i = 0
    
    while n > 0 and i < n:
        
        i += 1
        n -= i
    
    return i

def main():
    
    n = 11
    
    print(f"{arrangeCoins(n)}")
    
    return 0

if __name__ == '__main__':
    exit(main())
