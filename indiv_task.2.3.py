import random
ROUND_COUNT = 10
START, STOP = 1, 100

def lvl_dif(wish: int) -> int:  # Функция, которая выставляет сложность
    
    print('Выберите сложность, введя цифру от 1 до 4: \nЛегко - 1 \nСредне - 2 \nСложно - 3 \nНевозможно - 4')
    wish = input()
    
    attemp = 4  # количество попыток, ниже уровне сложности в зависимости от числа попыток
    easy = attemp * 5
    medium = attemp * 2
    difficult = attemp
    impossible = attemp // 2

    if wish == 1:
        round_count = easy
        print('Вы выбрали Лёгкий уровень, удачи.')
    elif wish == 2:
        round_count = medium
        print('Вы выбрали Средний уровень, приятной игры.')
    elif wish == 3:
        round_count = difficult
        print('Вы выбрали Сложный уровень, наслаждайтесь.')
    elif wish == 4:
        round_count = impossible
        print('Вы выбрали Невозможный уровень, страдайте.')
    else:
        print('Ошибка, повторите ввод, \nвводите только цифры от 1 до 4 включительно.')

"""def pool_num(start:int, stop:int) -> int:  # Функция, позволяющая выставить кастомный диапазон или начать игру со стоковым от 1 до 100
    
    print('Нажмите 0 если хотите ввести числовой диапазон, только натуральные числа.')
    setting = input()

    if setting == 0:
        start = input('Введите начало диапазона чисел')
        stop = input('Введите конец диапазона чисел')
        return start, stop
    else:
        start = 1
        stop = 100
        return start, stop"""
     



def configure_application():
  print('Нажмите 0 если хотите ввести числовой диапазон, только натуральные числа.')
  setting = input()
  
  if settings == 0:
    START, STOP = read_user_range()


def read_user_range() -> tuple[int, int]:  # Функция, позволяющая выставить кастомный диапазон или начать игру со стоковым от 1 до 100
    START = input('Введите начало диапазона чисел')
    STOP = input('Введите конец диапазона чисел')
    return START, STOP

  
def validate_input(txt: str) -> bool:
    """Функция, которая проверяет, что введённое число корректно.
    Если пользователь ввёл что-то не то, то печатает на экран, что не так."""

    if not txt.isdigit() or txt.startswith("0"):
        print(f'"{txt}" - не является целым положительным числом.')
        return False
        
    num = int(txt)
    if not START <= num <= STOP:
        print(f'Введенное число находится вне диапазона: {START} - {STOP}')
        return False

    return True


def check_result(answer: int, user_num: int) -> bool:
    if answer < user_num:
        print("Подсказка: Too much")
        return False
    if answer > user_num:
        print("Подсказка: It's no enough")
        return False
    
    return True

'''КОМИТ'''
def run_round(answer: int) -> bool:
    """ возвращаем True , если пользователь угадал, False иначе"""
    txt = input("your number: ")

    if not validate_input(txt):
      return False

    user_num = int(txt)

    return check_result(answer, user_num)

  
def main():
    # "привет, давай играть, количество попыток х , диапазон: [y,z], нажми enter чтобы начать, введи 0, чтобы настроить игру"
    # если вводит 0 , то запросить все зачения (пустой ввод означает, что он согласен с дефолтом)
    # введённые значения пользователя установят значения для глобальных переменных
    answer = random.randint(START, STOP)
    print("Угадай число от 1 до 100")
    print(answer)

    for round in range(ROUND_COUNT):
        print(f"Try: {round + 1}. \nОсталось попыток: {ROUND_COUNT - (round + 1)}")

        if run_round(answer):
            print("You WIN")
            return
          
    print("Game over")
    return
		       
main()