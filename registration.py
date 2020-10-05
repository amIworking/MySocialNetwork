#Приветствие
print("Добро пожаловать в соц. сеть ")

#Вопрос к пользователю
while True:
    q1 = input("Имеете ли вы аккаунт вы здесь уже здесь аккаунт? (ответ да или нет)\n")
    if q1 =="да":
        print("Я пока не умею считывать данные из файла, поэтому сделай вид, что ты тут новенький и зарегестрируйся")
        break
    if q1 == "нет":
        print("Отлично, го регаться")
        break
    else:
        print("Ты ввел что-то не то, ответ 'да' или 'нет'")

#Регистрация
while True:
    email = input("Введите ваш email-адрес:\n")
    if "@" not in email:
        print("Ваш email не содержит знак '@'\nПожалуйста, попробуйте еще раз")
    elif  email.split(".")[-1] not in ["ru", "com", "net", "ua", "kz"]:
        print("Ваш email не содержит доменов '.ru', '.com' и подобных\nПожалуйста, попробуйте еще раз")
    else:
        break
while True:
    nickname = input ("Придумайте свой никнейм:\n")
    if len(nickname) < 3:
        print("Ваш никнейм слишком короткий. Никнейм должен содержать от 3 символов\n")
    else:
        break
while True:
    password =  input ("Придумайте ваш пароль (от 6 символов):\n")
    if len(password) < 6:
        print("Ваш пароль слишком короткий. Пароль должен содержать от 6 символов\n")
    else:
        break
name = input("Введите ваше Имя:\n")
surname = input("Введите вашу Фамилию:\n")

#Запись всех данных в общий файл
f=open("id_number.txt")
data=f.read()
f.close()
f=open("id_number.txt", "w")
id= int(data) + 1
id=str(id)
f.write(id)
f.close()
data = [id, email, nickname, password, name, surname]
with open("data\data.txt", "a") as file:
    file.write(' '  + ' '.join(data))
    file.close()
print("Вы успешно зарегестрировались\n")

#Смена данных пользователя
print("Хотите ли вы изменить свои данные?")
ques = input("Если да, нажмите 1, если нет - 2:\n")
if ques == "1":
    print("Зайти в изменение")
if ques == "2":
    print("Ну окей, можешь не пользоваться моей фичей(")
else:
    print("Попробуйте снова")

