def main():
    mat = [[1,16,15,14,13,12],
        [2,17,24,23,22,11],
        [3,18,19,20,21,10],
        [4,5,6,7,8,9]]
    spiral = spiral_matrix(mat)
    spiral = rev(spiral)
    res = fill_matrix(spiral, len(mat[0]), len(mat))
    print(res)

        
def fill_matrix(matr: list, depth: int, length: int) -> list[list]:
    result = [[0] * depth for _ in range(length)]
    top, bottom = 0, length
    left, right = 0, depth - 1
    counter = 0
    while top < bottom and left <= right:
        for i in range(top, bottom):
            #print(mat[i][left])
            result[i][left] = matr[counter]
            counter += 1
        left += 1

        for j in range(top+1, right+1):
            #print(mat[bottom][j])
            result[bottom-1][j] = matr[counter]
            counter += 1
        bottom -= 1

        for k in range(bottom-1, top-1,-1):
            #print(mat[k][right])
            result[k][right] = matr[counter]
            counter += 1
        right -= 1
        for l in range(right, top,-1):
            #print(mat[top][l])
            result[top][l] = matr[counter]
            counter += 1
        top += 1
    return result


def spiral_matrix(matrix: list[list]) -> list:
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(top, bottom +1):
            #print(mat[i][left])
            result.append(matrix[i][left])
        left += 1

        for j in range(top+1, right+1):
            #print(mat[bottom][j])
            result.append(matrix[bottom][j])
        bottom -= 1

        for k in range(bottom, top-1,-1):
            #print(mat[k][right])
            result.append(matrix[k][right])
        right -= 1
        for l in range(right, top,-1):
            #print(mat[top][l])
            result.append(matrix[top][l])
        top += 1
    return result

def rev(li: list) -> list:
    leng = len(li) - 1
    result = [0] * (leng + 1)
    for i in range(len(li)):
        result[leng-i] = li[i]
    print("hello")
    return result

if __name__ == "__main__":
    main()

