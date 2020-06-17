import enlang
import rulang
import os
# очищаем текст в консоли для нашей программы
os.system("cls")

# выводим предупреждение о тексте
print('Set your language in file "lang.txt"')
print('Установите свой язык в файле "lang.txt"')
print(" ")

# открываем файл с настройками языка и записываем параметр
lang_file=open('lang.txt', 'r')
lang_main=lang_file.read(2)
lang_file.close

# присваиваем главным переменным с текстом языковую переменную
if lang_main=='en':
    lang_test='empty'
    # определяем название модуля, точка и название языковой перменной
    lang_test=enlang.enlang_test

# присваиваем главным переменным с текстом языковую переменную
if lang_main=='ru':
    lang_test='пусто'
    # определяем название модуля, точка и название языковой перменной
    lang_test=rulang.rulang_test

# выводим тестовое сообщение
print("--------------------------------------------------------------")
print(lang_test)
print("--------------------------------------------------------------")