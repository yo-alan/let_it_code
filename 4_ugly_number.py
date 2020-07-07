def ugly_number(n: int) -> int:
    
    ugly_numbers = [1]
    
    for i in range(n):
        
        un = ugly_numbers.pop(0)
        
        if un * 2 not in ugly_numbers:
            ugly_numbers.append(un * 2)
        
        if un * 3 not in ugly_numbers:
            ugly_numbers.append(un * 3)
        
        if un * 5 not in ugly_numbers:
            ugly_numbers.append(un * 5)
        
        ugly_numbers.sort()
    
    return un
    
    
def main():
    
    n = 10
    
    print(f"{ugly_number(n)}")
    
    return 0

if __name__ == '__main__':
    exit(main())
