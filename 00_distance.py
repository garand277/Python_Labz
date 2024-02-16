#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

for city1, cord1 in sites.items():
    distances[city1] = {}
    for city2, cord2 in sites.items():
        if city1 != city2:
            x = round(((cord1[0] - cord2[0]) ** 2 + (cord1[1] - cord2[1]) ** 2) ** 0.5, 2)
            distances[city1][city2] = x

print(distances)
