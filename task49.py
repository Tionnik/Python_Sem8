# Фамилия,Имя,Отчество,Телефон
import os

def show():                                                                     # Печать всей базы
    with open(FILE_PATH,'r',encoding='utf-8') as base:
        print(base.read())

def search():                                                                   # Поиск в базе
    searchValue=input("Введите строку поиска:")
    searchValue=searchValue.upper()                                             # Перевод искомого слова в верхний регистр
    with open(FILE_PATH,'r',encoding='utf-8') as base:
        for i in base.readlines():                                              # Чтение строки из файла                                          
            j=i.upper()                                                         # Перевод строки в верхний регистр для поиска
            if searchValue in j:                                                # По элементное сравнение строки с запросом поиска
                print(i)

def add():                                                                      # Добавление новой записи в файл
    family=input("Введите фамилию: ")
    name=input("Введите имя: ")
    lastname=input("Введите отчество: ")
    phone=input("Введите телефон: ")
    with open(FILE_PATH,'a',encoding='utf-8') as base:
        base.write(family+' '+name+' '+lastname+' '+phone+'\n')

def edit():                                                                     # Замена записи в файле
    index=int(input("Введите номер строки: "))                                  # Выбор строки для замены
    family=input("Введите фамилию: ")                                           # Заполняем новые данные для замены
    name=input("Введите имя: ")
    lastname=input("Введите отчество: ")
    phone=input("Введите телефон: ")
    with open(FILE_PATH,'r',encoding='utf-8') as base1:                         # Открытие базы для чтения
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as base2:                # Открытие временной базы для записи
            i=1
            while True:
                info=base1.readline()                                           # Построчно переписываем данные из базы чтения
                if info:                                                        # пока не закончатся строки
                    if index!=i:                                                # в базу для записи исключая строку для замены
                        base2.write(info)
                    else:
                        base2.write(family+' '+name+' '+lastname+' '+phone+'\n') # Заменяем данные в строке замены      
                else:
                    break
                i += 1
    os.remove(FILE_PATH)                                                        # Удаляем начальную базу
    os.rename(FILE_PATH_TEMP,FILE_PATH)                                         # Переименовываем временную базу на начальную

def delete():                                                                   # Удаление выбранной строки
    index=int(input("Введите номер строки: "))
    with open(FILE_PATH,'r',encoding='utf-8') as base1:
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as base2:
            i=1
            while True:
                info=base1.readline()
                if info:
                    if index!=i:
                        base2.write(info)
                else:
                    break
                i+=1
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TEMP,FILE_PATH)

FILE_PATH = r"Python_Sem8\base.txt"                                             # Начальная база
FILE_PATH_TEMP = r"Python_Sem8\base_temp.txt"                                   # Временная база
while True:                                                                     # Печать списка допустимых команд
    print('[1] Показать')
    print('[2] Поиск')
    print('[3] Добавить')
    print('[4] Редактировать')
    print('[5] Удалить')
    print('[6] Выход')
    print()
    res = int(input("Введите номер: "))

    if res ==1:                                                                 # Выполнение команды
        show()
    elif res==2:
        search()
    elif res==3:
        add()
    elif res==4:
        edit()
    elif res==5:
        delete()
    elif res==6:
        break


