def main():
    mat = [[1,16,15,14,13,12],
        [2,17,24,23,22,11],
        [3,18,19,20,21,10],
        [4,5,6,7,8,9]]
    matrice = load('movie-1-spiral.txt')
    spiral = spiral_matrix(matrice)
    spiral = rev(spiral)
    res = fill_matrix(spiral, len(matrice[0]), len(matrice))

        
def fill_matrix(matr: list, depth: int, length: int) -> list[list]:
        
    result = [[0] * depth for _ in range(length)] # pripravi matici na
    top, bottom = 0, length -1
    left, right = 0, depth - 1
    counter = 0
    while top <= bottom and left <= right:

        for i in range(top, bottom+1):
            #print(mat[i][left])
            result[i][left] = matr[counter]
            counter += 1
        left += 1

        for j in range(left, right+1):
            #print(mat[bottom][j])
            result[bottom][j] = matr[counter]
            counter += 1
        bottom -= 1
        if left <= right:  # Přidání podmínky pro případ, kdy matici oběhneme
            for k in range(bottom, top-1, -1):
                result[k][right] = matr[counter]
                counter += 1
            right -= 1

        if top <= bottom:  # Přidání podmínky
            for l in range(right, left-1, -1):
                result[top][l] = matr[counter]
                counter += 1
            top += 1

    upload_to_txt(result, len(result)-1, len(result[0])-1)
    return result


def spiral_matrix(matrix: list[list]) -> list:
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for i in range(top, bottom+1):
            result.append(matrix[i][left])
        left += 1

        for j in range(left, right+1):
            result.append(matrix[bottom][j])
        bottom -= 1

        if left <= right:  # Přidání podmínky pro případ, kdy matici oběhneme
            for k in range(bottom, top-1, -1):
                result.append(matrix[k][right])
                
            right -= 1

        if top <= bottom:  # Přidání podmínky
            for l in range(right, left-1, -1):
                result.append(matrix[top][l])
            top += 1

    upload_to_txt(result, len(result), len(result[0]))
    return result

def rev(li: list) -> list:
    leng = len(li) - 1
    result = [0] * (leng + 1)
    for i in range(len(li)):
        result[leng-i] = li[i]
    return result

def load(filename:str):
    array: list[list] = []
    with open(filename) as f:
       for line in f:
           line = line.strip() # odebere \n na konci
           row = list(line) #doplni radky
           array.append(row)
    return array


def upload_to_txt(image: list, rows, cols):
    with open('image.txt','w') as f:
        for i in range(rows):
            for j in range(cols):
                f.write(str(image[i][j]))
            f.write('\n')

if __name__ == "__main__":
    main()

