# geometric_lib

Небольшая библиотека для вычисления площади и периметра круга, квадрата и прямоугольника.

## Модули и функции

- `circle.area(r)` — площадь круга: πr².
- `circle.perimeter(r)` — длина окружности: 2πr.
- `square.area(a)` — площадь квадрата: a².
- `square.perimeter(a)` — периметр квадрата: 4a.
- `rectangle.area(a, b)` — площадь прямоугольника: ab.
- `rectangle.perimeter(a, b)` — периметр прямоугольника: 2(a+b).

Для отрицательных значений размеров функции выбрасывают `ValueError`. Нулевые размеры допустимы.

## Запуск тестов

Из корневой папки проекта выполните:

```bash
python -m unittest discover -s tests -v
```

## CI

GitHub Actions запускает тесты при каждом `push` на runner'ах `ubuntu-latest` и `windows-latest`.
Конфигурация находится в `.github/workflows/main.yml`.
