'''1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
'''

# Крестики-нолики в графике и внутри venv
import tkinter
from tkinter import Tk, messagebox

matrix = [[' ' for y in range(3)] for x in range(3)]
button = [[' ' for y in range(3)] for x in range(3)]
flag = True
count = 0


def click(x, y):
    global count
    global flag
    if flag and matrix[x][y] == ' ' and count % 2 == 0:
        matrix[x][y] = 'X'
        button[x][y].configure(text="X")
        count += 1
        win_checker('X')
    elif flag and matrix[x][y] == ' ' and count % 2 != 0:
        matrix[x][y] = 'O'
        count += 1
        button[x][y].configure(text="O")
        win_checker('O')


def win_checker(val):
    global flag
    for im in range(3):
        if matrix[im][0] == matrix[im][1] == matrix[im][2] and matrix[im][0] != ' ':
            flag = False
            winner = messagebox.showinfo("Победа!", val + " Победили!")
            break
        elif matrix[0][im] == matrix[1][im] == matrix[2][im] != ' ':
            flag = False
            winner = messagebox.showinfo("Победа!", val + " Победили!")
            break
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != ' ':
        flag = False
        winner = messagebox.showinfo("Победа!", val + " Победили!")

    if matrix[0][2] == matrix[1][1] == matrix[2][0] != ' ':
        flag = False
        winner = messagebox.showinfo("Победа!", val + " Победили!")



root = Tk()
root.title("Tic Tac Toe")


for x in range(3):
    line = []
    for y in range(3):
        button[x][y] = tkinter.Button(root, text=' ', width=4, height=2, font=('Verdana', 20, 'bold'),
                                      background='lavender',
                                      command=(lambda x=x, y=y: click(x, y)))
        button[x][y].grid(row=x, column=y, sticky='nsew')
        line.append(button[x][y])
    matrix.append(line)

root.mainloop()
