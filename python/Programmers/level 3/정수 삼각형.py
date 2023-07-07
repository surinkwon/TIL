def solution(triangle):
    
    for r in range(1, len(triangle)):
        end = len(triangle[r]) - 1
        triangle[r][0] += triangle[r - 1][0]
        triangle[r][end] += triangle[r - 1][end - 1]
        
        for c in range(1, end):
            triangle[r][c] += max(triangle[r - 1][c - 1], triangle[r - 1][c])
    
    return max(triangle[len(triangle) - 1])