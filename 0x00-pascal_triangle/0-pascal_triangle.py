def pascal_triangle(n):
    triangle = []
    if n <= 0:
        triangle.append([])
    elif n == 1:
        triangle.append([1])
    elif n == 2:
        triangle.append([1])
        triangle.append([1,1])
    else:
        triangle.append([1])
        triangle.append([1,1])
        for i in range(2, n):
            sub = []
            sub.append(1)
            for j in range(0, i-1):
                sub.append(triangle[i-1][j] + triangle[i-1][j+1])
            sub.append(1)
            triangle.append(sub)

            
    # print(triangle)
    return triangle
