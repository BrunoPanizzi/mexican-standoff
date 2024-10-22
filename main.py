import sys
import time


[size, b, c] = [int(i) for i in sys.argv[1:]]

print(size, b, c)

tabuleiro = [[None for _ in range(size)] for _ in range(size)]

# tabuleiro[0][0] = 'a'
# tabuleiro[-1][-1] = 'a'
# tabuleiro[4][4] = 'b'
# tabuleiro[-2][4] = 'a'
# tabuleiro[-1][4] = 'b'


def valido(tabuleiro):
    for i, line in enumerate(tabuleiro):
        for j, col in enumerate(line):
            if col is not None and not verifica(tabuleiro, col, i, j):
                return False
    return True

#                   l  c
def verifica(tabuleiro, letra, i, j):
    # letra = tabuleiro[i][j]

    # ←←←←
    for k in range(j-1, -1, -1):
        w = tabuleiro[i][k]
        if w == letra:
            # print("não foi no ←←←←")
            return False
        if w is not None and w != letra:
            break

    # →→→→
    for k in range(j+1, size):
        w = tabuleiro[i][k]
        if w == letra:
            # print("não foi no →→→→")
            return False
        if w is not None and w != letra:
            break

    # ↑↑↑↑
    for k in range(i-1, -1, -1):
        w = tabuleiro[k][j]
        if w == letra:
            # print("não foi no ↑↑↑↑")
            return False
        if w is not None and w != letra:
            break

    # ↓↓↓↓
    for k in range(i+1, size):
        w = tabuleiro[k][j]
        if w == letra:
            # print("não foi no ↓↓↓↓")
            return False
        if w is not None and w != letra:
            break

    # ←↑←↑
    k = 0
    while i-k > 0 and j-k > 0:
        k += 1
        w = tabuleiro[i-k][j-k]
        if w == letra:
            # print("não foi no ←↑←↑")
            return False
        if w is not None and w != letra:
            break

    # →↑→↑
    k = 0
    while i-k > 0 and j+k < size-1:
        k += 1
        w = tabuleiro[i-k][j+k]
        if w == letra:
            # print("não foi no →↑→↑")
            return False
        if w is not None and w != letra:
            break

    # ←↓←↓
    k = 0
    while i+k < size-1 and j-k > 0:
        k += 1
        w = tabuleiro[i+k][j-k]
        if w == letra:
            # print("não foi no ←↓←↓")
            return False
        if w is not None and w != letra:
            break

    # →↓→↓
    k = 0
    while i+k < size-1 and j+k < size-1:
        k += 1
        w = tabuleiro[i+k][j+k]
        if w == letra:
            # print("não foi no →↓→↓")
            return False
        if w is not None and w != letra:
            break

    return True


def copy_tabuleiro(tabuleiro):
    return [[i for i in line] for line in tabuleiro]


def print_tabuleiro(tabuleiro):
    print("+", end="")
    print("-"*size*2, end="+\n")
    for line in tabuleiro:
        print("|", end="")
        for col in line:
            if col is None:
                print("  ", end="")
            else:
                print(f"{col} ", end="")
        print("|")
    print("+", end="")
    print("-"*size*2, end="+\n")


def faz(tabuleiro, b, c, last_c: str, last_pos: (int, int)):
    if not valido(tabuleiro):
        print('not valido')
        tabuleiro[last_pos[0]][last_pos[1]] = None
        if last_c == 'b':
            b += 1
        if last_c == 'c':
            c += 1
        return False

    if b <= 0 and c <= 0:
        return

    for i in range(size*size*2):
        j = i >> 1
        line = j // size
        col = j % size
        if tabuleiro[line][col] is not None:
            continue
        if i % 2 == 0 and b > 0:  # bigodudo
            tabuleiro[line][col] = 'b'
            # b -= 1
            print(f"fazendo com b em [{line}][{col}]")
            faz(copy_tabuleiro(tabuleiro), b-1, c, 'b', (line, col))
        elif i % 2 == 1 and c > 0:           # capeta
            tabuleiro[line][col] = 'c'
            # c -= 1
            print(f"fazendo com c em [{line}][{col}]")
            faz(copy_tabuleiro(tabuleiro), b, c-1, 'c', (line, col))
            # faz('c', (line, col))

        clear()
        print_tabuleiro(tabuleiro)
        print(f"{b=}, {c=}, {i=}, {size=}")
        # input()
        time.sleep(0.01)

        # desfaz
        tabuleiro[line][col] = None


def clear():
    print(chr(27) + "[2J")


faz(tabuleiro, b, c, None, (0, 0))

#   char, line, col
# pilha = []
# while True:
#     clear()
#     print_tabuleiro()
#     if b > 0:
#         popado = ('', 0, 0)
#         if len(pilha) != 0:
#             popado = pilha.pop()
#         c, i, j = popado

#         j += 1
#         next = ('b', i + j//size, j % size)

#     input()


# clear()
# print_tabuleiro()
# input()
# clear()

# print(valido())





# copia ultimo movimento
# adiciona movimento atual
# se for válido, continua
# se não, vai para a próxima casa


# pop ultimo movimento
# verifica movimento atual
# se for válido, adiciona popado e atual
# se não, vai para a próxima casa

