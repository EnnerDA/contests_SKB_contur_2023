# contests_SKB_contur_2023
[Условия задач](https://github.com/skbkontur/contests/blob/main/internship_cs_mar23/statements.pdf)

[Задача D. Общительный человек.](https://github.com/EnnerDA/contests_SKB_contur_2023/blob/main/D.py)

[Задача E. Неплохой огородник.](https://github.com/EnnerDA/contests_SKB_contur_2023/blob/main/E.py)

**В худщем варианте** (где нет сорняков высотой 9, либо он один и находится в самой нижней правой клетке поля) - **O(N\*M)**. 

Мы 5 раз пробежимся по всему массиву в поисках максимума. При условии N,M <=1400, общее колисество действий ~ 10 млн. операций

**В лучшеи случае** (если в позициях (1,1), (1,2), (2,1) сорняки высотой 9) -  **O(1)** 

