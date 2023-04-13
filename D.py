# приём данных
f = open('input.txt', 'r')
N = int(f.readline())
ans = [{0, }, ]


def next_cube(val_list: list, cube: set) -> None:
    """Функция принимает уже существущий список возможных чисел,
    и следующий кубик. Создает set() возможных чисел с учетом нового кубика
    и добавляет его последним элементом в список возможных чисел"""
    temp_val_list = set()
    for val in val_list[-1]:
        for cube_val in cube:
            temp_val_list.add(cube_val + val)
    ans.append(temp_val_list)


for _ in range(N):
    a = set(map(int, f.readline().split()))
    next_cube(ans, a)

print(len(ans[-1]))

f.close()
