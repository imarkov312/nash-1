__**Описание задания и подхода к его решению.**__

Задание состоит в численном решении матричной игры. 

Для решения была написана функция nash_equlibrium(a), где а - матрица выигрыша.
Функция возвращает следующие значения: 
1. Значение игры: v 
2. Оптимальные стратегии первого игрока: p
3. Оптимальные стратегии второго игрока: q

Решение матричной игры было сведено к решению пары двойственных задач линейного программирования.




> From this repository you can download package _**nash**_.
> There is a function in the package called **nash_equilibrium** which solves antagonistic matrix game


> You can download this package using _**pip**_ :
```
pip install git+git://github.com/smvlx/nash
```
