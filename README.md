# Игра в города

Консольная игра в города для двух игроков, написанная на Python. Игроки по очереди называют города, где каждый следующий город должен начинаться на последнюю букву предыдущего города.

## Описание

Игра реализует классические правила игры в города:
- Игроки ходят по очереди
- Каждый новый город должен начинаться с последней буквы предыдущего города
- Нельзя использовать уже названные города
- Можно использовать только реально существующие города из предоставленного списка

## Требования

- Python 3.6 или выше
- Файл `cities.txt` со списком городов в кодировке UTF-8

## Установка

1. Склонируйте репозиторий:
```bash
git clone https://github.com/your-username/cities-game.git
cd cities-game
```

2. Создайте файл `cities.txt` в корневой директории проекта и заполните его списком городов (по одному городу на строку).

## Использование

1. Запустите игру:
```bash
python game.py
```

2. Следуйте инструкциям в консоли:
   - Первый игрок вводит любой город
   - Второй игрок вводит город на последнюю букву города первого игрока
   - И так далее, пока один из игроков не сдастся или не закончатся подходящие города

Для завершения игры нажмите Ctrl+C.

## Особенности

- Автоматическая проверка существования городов
- Отслеживание использованных городов
- Проверка правильности ввода (город должен начинаться с последней буквы предыдущего города)
- Нечувствительность к регистру букв
- Обработка исключений при некорректном вводе

## Структура файлов

```
cities-game/
│
├── game.py         # Основной файл игры
├── cities.txt      # Список городов
└── README.md       # Документация
```

## Пример игры

```
Игрок 1, введите город: Москва
Игрок 2, введите город, начинающийся с последней буквы города Игрока 1: Архангельск
Игрок 2, Архангельск, правильно!
Игрок 1, введите город, начинающийся с последней буквы города Игрока 2: Казань
Игрок 1, Казань, правильно!
```

## Лицензия

MIT License. Подробности в файле LICENSE.
