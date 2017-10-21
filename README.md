## **Описание задания**

Задание состоит в численном решении антагонистической матричной игры. То есть, формально, нужно найти значение игры и оптимальные стратегии первого и второго игроков.

## **Подход к Решению**
Для решения была написана функция nash_equlibrium(a), где а - матрица выигрыша.
Функция возвращает следующие значения: 
1. Значение игры: v 
2. Оптимальные стратегии первого игрока: p
3. Оптимальные стратегии второго игрока: q

Решение матричной игры было сведено к решению пары двойственных задач линейного программирования.
Иными словами, задача была разбита на 2 подзадачи, каждая из которых заключалась в нахождении оптимальных стратегий для 1 и 2 игроков соответсвенно.

## Инструкция по запуску
Решение задание реализовано в виде пакета **nash**, который находится в папке

```submissions/task1/blokhina-smirnov```


> From this repository you can download package _**nash**_.
> There is a function in the package called **nash_equilibrium** which solves antagonistic matrix game


> You can download this package using _**pip**_ :
```
pip install git+git://github.com/smvlx/nash
```
