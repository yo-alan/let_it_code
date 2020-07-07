def prisonAfterNDays(cells: list, N: int):
    
    print(f"Day {0}: {cells}")
    
    N = 14 if N % 14 == 0 else N % 14
    
    for i in range(N):
        
        cells = [0] + [abs(abs(cells[j-1] - cells[j+1]) - 1) for j in range(1, len(cells)-1)] + [0]
        
        print(f"Day {i+1}: {cells}")
    
    return cells
    
    
def main():
    
    cells, n = [0,1,0,1,1,0,0,1], 7
    cells, n = [1,0,0,1,0,0,1,0], 1000000000
    
    print(f"{prisonAfterNDays(cells, n)}")
    
    return 0

if __name__ == '__main__':
    exit(main())
