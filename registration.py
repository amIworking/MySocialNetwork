from functions import *
from authorization import checking
from edit_account import edit
#Приветствие
print("Добро пожаловать в соц. сеть ")

#Вопрос к пользователю
while True:
    q1 = input("Имеете ли вы аккаунт вы здесь уже здесь аккаунт? (ответ да или нет)\n")
    if q1 =="да":
        checking()
        break
    if q1 == "нет":
        print("Отлично, го регаться")
        id()
        email()
        nickname()
        password()
        name = input("Введите ваше Имя:\n")
        surname = input("Введите вашу Фамилию:\n")
        break
    else:
        print("Ты ввел что-то не то, ответ 'да' или 'нет'")

#Регистрация


#Запись всех данных в общий файл
write_data()
print("Вы успешно зарегестрировались\n")

#Смена данных пользователя
print("Хотите ли вы изменить свои данные?")
ques = input("Если да, нажмите 1, если нет - 2:\n")
if ques == "1":
    edit()
if ques == "2":
    print("Ну окей, можешь не пользоваться моей фичей(")
else:
    print("Попробуйте снова")

