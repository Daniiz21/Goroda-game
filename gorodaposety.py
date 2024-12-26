import os

# Чтение списка городо
def load_cities():
    # Определяем абсолютный путь к файлу
    file_path = os.path.abspath('cities.txt')
    
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден. Убедитесь, что файл существует.")
        return set()  # Возвращаем пустое множество, если файл не найден
    
    # Открываем файл и читаем города
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file)

def play_city_game():
    cities = load_cities()  # Загружаем города из файла в множество для быстрого поиска
    if not cities:
        return  # Если городов нет (файл не найден или пуст), выходим из игры
    
    used_cities = set()  # Множество для хранения уже использованных городов

    # Запрос первого города у Игрока 1 с проверкой
    while True:
        player1_city = input("Игрок 1, введите город: ").title()
        
        # Проверка на существование города в списке и на то, что он не был использован
        if player1_city not in cities:
            print("Этот город не существует. Пожалуйста, введите существующий город.")
        elif player1_city in used_cities:
            print(f"Город {player1_city} уже был использован. Попробуйте другой.")
        else:
            used_cities.add(player1_city)  # Добавляем город в список использованных
            break  # Выход из цикла, если город корректный

    while True:
        try:
            player2_city = input("Игрок 2, введите город, начинающийся с последней буквы города Игрока 1: ").title()

            # Проверка на существование города и на то, что он не был использован
            if player2_city not in cities:
                print(f"Города {player2_city} не существует. Попробуйте снова.")
                continue
            if player2_city in used_cities:
                print(f"Город {player2_city} уже был использован. Попробуйте другой.")
                continue
            
            # Normalize both cities to lowercase for comparison
            if player2_city.lower().startswith(player1_city[-1].lower()):
                print(f"Игрок 2, {player2_city}, правильно!")
                used_cities.add(player2_city)  # Добавляем город в список использованных
                player1_city = input("Игрок 1, введите город, начинающийся с последней буквы города Игрока 2: ").title()
                
                # Проверка на существование города и на то, что он не был использован
                if player1_city not in cities:
                    print(f"Города {player1_city} не существует. Попробуйте снова.")
                    continue
                if player1_city in used_cities:
                    print(f"Город {player1_city} уже был использован. Попробуйте другой.")
                    continue

                if player1_city.lower().startswith(player2_city[-1].lower()):
                    print(f"Игрок 1, {player1_city}, правильно!")
                    used_cities.add(player1_city)  # Добавляем город в список использованных
                else:
                    print("Игрок 1, неверный город. Пожалуйста, попробуйте снова.")
            else:
                print("Игрок 2, неверный город. Пожалуйста, попробуйте снова.")
        
        except KeyboardInterrupt:
            # Обработка исключения при нажатии Ctrl + C
            print("\nИгра завершена.")
            break  # Завершаем игру

play_city_game()
