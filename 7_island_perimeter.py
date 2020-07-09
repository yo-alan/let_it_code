def island_perimeter(grid: list) -> int:
    
    seen = set()
    count = 0
    for l in grid:
        for i, x in enumerate(l):
            if x == 1:
                count += 4
                if i in seen:
                    count -= 2
                if i-1 in seen:
                    count -= 2
                seen.add(i)
            else:
                seen.discard(i)
    
    return count

def main():
    
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0],
    ]
    
    print(f"{island_perimeter(grid)}")
    
    return 0

if __name__ == '__main__':
    exit(main())
