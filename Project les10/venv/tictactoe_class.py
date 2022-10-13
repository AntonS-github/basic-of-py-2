class Tictactoe:
    def game(self):
        matrix = [['_' for y in range(3)] for x in range(3)]
        print(matrix)
        for im in range(3):
            print(matrix[im])
        flag = True
        while flag:
            cross = input('Игрок-1 введите координаты Х в формете "x y": ').split()
            x1, y1 = int(cross[0]), int(cross[1])
            matrix[x1 - 1][y1 - 1] = 'X'
            for im in range(3):
                print(matrix[im])
                col = [string[im] for string in matrix]  # columns
                diag_r = [matrix[i][i] for i in range(3)]  # diagonal right
                diag_l = [matrix[2 - i][i] for i in range(3)]  # diagonal left
                if len(list(set(matrix[im]))) == 1 and matrix[im][0] != '_':
                    print(f'Победили {matrix[im][0]}!')
                    flag = False
                    break
                elif len(list(set(col))) == 1 and col[0] != '_':
                    print(f'Победили {col[0]}!')
                    flag = False
                    break
                elif len(list(set(diag_r))) == 1 and diag_r[0] != '_':
                    print(f'Победили {diag_r[0]}!')
                    flag = False
                    break
                elif len(list(set(diag_l))) == 1 and diag_l[0] != '_':
                    print(f'Победили {diag_l[0]}!')
                    flag = False
                    break

            nought = input('Игрок-2 введите координаты O в формете "x y": ').split()
            x2, y2 = int(nought[0]), int(nought[1])
            matrix[x2 - 1][y2 - 1] = 'O'
            for im in range(3):
                print(matrix[im])
                col = [string[im] for string in matrix]  # columns
                diag_r = [matrix[i][i] for i in range(3)]  # diagonal right
                diag_l = [matrix[2 - i][i] for i in range(3)]  # diagonal left
                if len(list(set(matrix[im]))) == 1 and matrix[im][0] != '_':
                    print(f'Победили {matrix[im][0]}!')
                    flag = False
                    break
                elif len(list(set(col))) == 1 and col[0] != '_':
                    print(f'Победили {col[0]}!')
                    flag = False
                    break
                elif len(list(set(diag_r))) == 1 and diag_r[0] != '_':
                    print(f'Победили {diag_r[0]}!')
                    flag = False
                    break
                elif len(list(set(diag_l))) == 1 and diag_l[0] != '_':
                    print(f'Победили {diag_l[0]}!')
                    flag = False
                    break


s = Tictactoe()
s.game()
