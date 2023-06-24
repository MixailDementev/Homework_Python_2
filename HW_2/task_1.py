# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

def to_hex(num):
    hex_chars = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_chars[num % 16] + hex_str
        num //= 16
    return hex_str

num = int(input('Input number: '))

print(to_hex(num))


hex_str1 = hex(num)
print(hex_str1)
