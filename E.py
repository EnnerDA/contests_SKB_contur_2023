# приём данных
f = open('input.txt', 'r')
N, M = map(int, f.readline().split())
a = [tuple(map(int, list(f.readline().strip()))) for _ in range(N)]
f.close()


def find_max(field: list, minus_row: int = -1, minus_col: int = -1) -> (int, int, int):
    """Функция вернет кортеж с тремя значениями: максимальное число, и его координаты
    (номер столбца, номер строки) в заданном массиве field.
    Реализованны допольнительные опции:
     - исключения из поиска заданного ряда (minus_row)
     - исключения из поиска заданной строки (minus_col)
     - исключение из поиска и ряда и строки одновременно
    Нумерация столбцов и строк начинается с 0.
    """
    temp_max = 0
    r, c = 0, 0
    for row in range(len(field)):
        if minus_row != -1:
            if row == minus_row:
                continue
        for col in range(len(field[0])):
            if minus_col != -1:
                if col == minus_col:
                    continue
            #print(field[row][col], end = ' ')
            if field[row][col] == 9:
                r = row
                c = col
                temp_max = 9
                break
            elif field[row][col] > temp_max:
                r = row
                c = col
                temp_max = field[row][col]
        if temp_max == 9:
            break
        #print()
    return temp_max, r, c


max0, r0, c0 = find_max(a)

# если удалим r0:
c1 = find_max(a, minus_row=r0)[2]
max1 = find_max(a, minus_row=r0, minus_col=c1)[0]
var1 = (r0, c1, max1)

# если удалим с0:
r2 = find_max(a, minus_col=c0)[1]
max2 = find_max(a, minus_row=r2, minus_col=c0)[0]
var2 = (r2, c0, max2)

# выбираем оптимальный вариант:
# так как по условию задачи нуерация строк начинаеся с 1 к финальному значению добавлям 1
if var1[2] <= var2[2]:
    print(var1[0] + 1, var1[1] + 1)
else:
    print(var2[0] + 1, var2[1] + 1)
