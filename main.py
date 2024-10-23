import sys
import time


[size, b, c] = [int(i) for i in sys.argv[1:]]

print(size, b, c)

tabuleiro = [[None for _ in range(size)] for _ in range(size)]


def valido():
    for i, line in enumerate(tabuleiro):
        for j, col in enumerate(line):
            if col is not None and not verifica(col, i, j)[0]:
                return False
    return True


def veri_good():
    for i, line in enumerate(tabuleiro):
        for j, col in enumerate(line):
            if col is not None:
                valido, inimigos = verifica(col, i, j)
                if not valido or inimigos < 2:
                    return False
    return True


def verifica_direcao(letra, i, j, di, dj) -> (bool, bool):
    while 0 < i <= size and 0 < j <= size:
        i += di
        j += dj

        w = tabuleiro[i][j]

        if w == letra:
            return False, False
        if w is not None and w != letra:
            return True, True

    return True, False


def verifica(letra, i, j) -> (bool, int):
    # letra = tabuleiro[i][j]
    ve = 0

    # ←←←←
    for k in range(j-1, -1, -1):
        w = tabuleiro[i][k]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    # →→→→
    for k in range(j+1, size):
        w = tabuleiro[i][k]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    # ↑↑↑↑
    for k in range(i-1, -1, -1):
        w = tabuleiro[k][j]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    # ↓↓↓↓
    for k in range(i+1, size):
        w = tabuleiro[k][j]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    # ←↑←↑
    k = 0
    while i-k > 0 and j-k > 0:
        k += 1
        w = tabuleiro[i-k][j-k]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    # →↑→↑
    k = 0
    while i-k > 0 and j+k < size-1:
        k += 1
        w = tabuleiro[i-k][j+k]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    # ←↓←↓
    k = 0
    while i+k < size-1 and j-k > 0:
        k += 1
        w = tabuleiro[i+k][j-k]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    # →↓→↓
    k = 0
    while i+k < size-1 and j+k < size-1:
        k += 1
        w = tabuleiro[i+k][j+k]
        if w == letra:
            return (False, ve)
        if w is not None and w != letra:
            ve += 1
            break

    return (True, ve)




def desenha_tabuleiro(tabuleiro):
    buf = ""

    buf += "+"
    buf += "-"*size*2 + "+\n"

    for line in tabuleiro:
        buf += "|"
        for col in line:
            if col is None:
                buf += "  "
            else:
                buf += col + " "
        buf += "|\n"

    buf += "+"
    buf += "-"*size*2 + "+\n"

    return buf


def print_tabuleiro(tabuleiro):
    print(desenha_tabuleiro(tabuleiro))


bom = 0


def faz(b, c, last_i: int):
    global verificados
    last_line = (last_i >> 1) // size
    last_col = (last_i >> 1) % size

    if not valido():
        tabuleiro[last_line][last_col] = None
        return

    if b <= 0 and c <= 0:
        if veri_good():
            global bom
            bom += 1
        return

    for i in range(last_i, size*size*2):
        j = i >> 1
        line = j // size
        col = j % size
        if tabuleiro[line][col] is not None:
            continue
        if i % 2 == 0 and b > 0:      # bigodudo
            tabuleiro[line][col] = 'b'
            faz(b-1, c, i)
        elif i % 2 == 1 and c > 0:    # capeta
            tabuleiro[line][col] = 'c'
            faz(b, c-1, i)

        # clear()
        # print_tabuleiro(tabuleiro)
        # print(f"{bom=}")
        # input()
        # time.sleep(0.01)

        tabuleiro[line][col] = None


def clear():
    print(chr(27) + "[2J")


faz(b, c, 0)

print(f"{bom=}")
