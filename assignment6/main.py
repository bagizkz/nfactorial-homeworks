def expercise_1():
    print ('--Expercise 1')
    ex1_num_1 = 15
    ex1_num_2 = 17
    ex1_math = ex1_num_1 + ex1_num_2
    print ('Сумма:', ex1_math)
    print ('Expercise 1 END\n')

def expercise_2():
    print('--Expercise 2')
    ex2_text = 'Salem'
    ex2_text_rev = ex2_text[::-1]
    print ('Перевернутая строка "Salem":', ex2_text_rev)
    print ('Expercise 2 END\n')

def expercise_3():
    print('-- Expercise 3')
    ex3_text = len('Salem')
    print('Длина строки "Salem": ', ex3_text)
    print ('Expercise 3 END\n')

def expercise_4():
    print('-- Expercise 4')
    ex4_text1 = 'Salem'
    ex4_text2 = 'Alem'
    ex4_result = ex4_text1 + " " + ex4_text2
    print(f'Объединеная строка: {ex4_result}')
    print('Expercise 4 END\n')

def expercise_5():
    print('--Expercise 5')
    ex5_char = 'Ж'
    is_vowel = ex5_char.lower() in 'а, у, о, и, э, ы'
    ex5_result = "является" if is_vowel else "не является"
    print(f"Символ '{ex5_char}' {ex5_result} гласной")
    print('Expercise 5 END\n')

def expercise_6():
    print('--Expercise 6')
    ex6_text = 'Salem'
    ex6_text_swap = ex6_text[-1] + ex6_text[1:-1] + ex6_text[0]
    print(f"Измененная строка 'Salem'> {ex6_text_swap}")
    print('Expercise 6 END\n')

def expercise_7():
    print('--Expercise 7')
    exp7_text = 'salem'
    exp7_text_upper = exp7_text.upper()
    print(f"Cтрока в верхнем: {exp7_text_upper}")
    print('Expercise 7 END\n')

def expercise_8():
    print('--Expercise 8')
    ex8_length = 5
    ex8_width = 10
    ex8_result = ex8_length * ex8_width
    print(f"Площадь прямоугольника: {ex8_result}")
    print('Expercise 8 END\n')

def expercise_9():
    print('--Expercise 9')
    ex8_num = 3
    ex8_read = ex8_num % 2 == 0
    ex8_result = "четное" if ex8_read else "не четное"
    print (f'{ex8_num} - это {ex8_result}')
    print('Expercise 9 END\n')

def expercise_10():
    print('--Expercise 10')
    ex10_text = "Salem"
    ex10_chars = ex10_text[:3]
    print(f'Первые три символа "Salem": {ex10_chars}')
    print('Expercise 10 END\n')

def expercise_11():
    print('--Expercise 10')
    ex11_name = 'Baglan'
    ex11_age = 33
    ex11_msg = f'Меня зовут {ex11_name}, мне {ex11_age} лет'
    print(ex11_msg)
    print('Expercise 10 END\n')

def expercise_12():
    print('--Expercise 12')
    ex12_text = "Salem, Alem!"
    ex12_string = ex12_text[2:6]
    print(f'Извлеченные символы "Salem, Alem!": {ex12_string}')
    print('Expercise 12 END\n')

def expercise_13():
    print('--Expercise 13')
    ex12_text = '1991'
    ex12_to_int = int(ex12_text)
    print('Строка стала числом:', ex12_to_int)
    print('Expercise 12 END\n')

def expercise_14():
    print('--Expercise 13')
    ex14_text = 'Salem'
    ex14_repart = ex14_text * 3
    print(f'Повтор строки {ex14_repart}')
    print('Expercise 12 END\n')


## 15 Вернуться позже
def expercise_15():
    print('--Expercise 15')
    ex15_num1 = 9
    ex15_num2 = 4
    ex15_quot = ex15_num1 // ex15_num2
    ex15_rem = ex15_num1 % ex15_num2
    print(f'Числа 9 и 4. quotient: {ex15_quot} remainder: {ex15_rem}')
    print('Expercise 15 END\n')



def expercise_16():
    print('--Expercise 16')
    ex16_num1 = 10
    ex16_num2 = 4
    ex16_float = float(ex16_num1) / float(ex16_num2)
    print(f'Результат с плавующей точкой: {ex16_float}')
    print('Expercise 16 END\n')


def expercise_17():
    print('--Expercise 17')
    ex17_text = 'Qanagatandyrlmagandyqtarynyzdan'
    ex17_count = ex17_text.count('a')
    print(f'В слове "{ex17_text}" букв "a" = {ex17_count}')
    print('Expercise 17 END\n')



def expercise_18():
    print('--Expercise 18:')
    ex18_text = "Salem \"nFactorial\""
    print(f'Строка с ковычками: {ex18_text}')
    print('Expercise 18 END\n')


def expercise_19():
    print('--Expercise 19:')
    ex19_multi_line = """Строка 1
    Строка 2
    Строка 3"""
    print(ex19_multi_line)
    print('Expercise 19 END\n')


def expercise_20():
    print('--Expercise 20:')
    ex20_base = 2
    ex20_exponent = 3
    ex20_result = ex20_base ** ex20_exponent
    print(f"{ex20_base} в степени {ex20_exponent} равно {ex20_result}")
    print('Expercise 20 END\n')


def main():
    expercise_1()
    expercise_2()
    expercise_3()
    expercise_4()
    expercise_5()
    expercise_6()
    expercise_7()
    expercise_8()
    expercise_9()
    expercise_10()
    expercise_11()
    expercise_12()
    expercise_13()
    expercise_14()
    expercise_15()
    expercise_16()
    expercise_17()
    expercise_18()
    expercise_19()
    expercise_20()

if __name__ == "__main__":
    main()