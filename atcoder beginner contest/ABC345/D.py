def check_covered(grid, tiles):
    covered = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for tile in tiles:
        for i in range(tile[0]):
            for j in range(tile[1]):
                if grid[i][j] and not covered[i][j]:
                    covered[i][j] = True
                else:
                    return False
    for row in covered:
        if False in row:
            return False
    return True

def can_cover_all(grid, tiles):
    for tile in tiles:
        if tile[0] <= len(grid) and tile[1] <= len(grid[0]):
            rotated_tile = (tile[1], tile[0])
            for i in range(len(grid) - tile[0] + 1):
                for j in range(len(grid[0]) - tile[1] + 1):
                    if check_covered([row[j:j + tile[1]] for row in grid[i:i + tile[0]]], [tile, rotated_tile]):
                        return True
    return False

def main():
    H, W, N = map(int, input().split())
    tiles = [tuple(map(int, input().split())) for _ in range(N)]
    grid = [[False] * W for _ in range(H)]

    if can_cover_all(grid, tiles):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()