f = open("data\data.txt")
dataBases=f.read()
accounts = dataBases.split(" ")
f.close()
f = open("userData.txt")
dataBases=f.read()
userData = dataBases.split(" ")
f.close()
data=userData.copy()


print("Что из перечисленного вы хотите изменить?")
while True:
    choice = input("1  -- email\n2 -- никнейм\n3 -- пароль\n4 -- имя\n5 -- фамилию\n")
    mas = ["1","2","3","4","5"]
    if choice not in mas:
        print("Тут не предусмотрена эта функция, попробуйте снова")
    else:
        title = ["email", "nickname", "пароль", "имя", "фамилия"]
        dell = data[int(choice)]
        if int(choice) in range(1, 3):
            while True:
                chec = input("Введите пароль для подверждения\n")
                if chec != data[3]:
                    print("Указан неверный пароль, в доступе отказано. Попробуйте снова")
                else:
                    break
        print("Вы выбрали " + dell)
        data.remove(dell)
        if choice == "1":
            while True:
                new = input("Введите ваш новый email-адрес:\n")
                password = new
                if "@" not in new:
                    print("Ваш email не содержит знак '@'\nПожалуйста, попробуйте еще раз")
                elif new.split(".")[-1] not in ["ru", "com," "net", "ua", "kz"]:
                    print("Ваш email не содержит доменов '.ru', '.com' и подобных\nПожалуйста, попробуйте еще раз")
                else:
                    break
        if choice == "2":
            while True:
                new = input("Придумайте свой никнейм:\n")
                nickname = new
                if len(new) < 3:
                    print("Ваш никнейм слишком короткий. Никнейм должен содержать от 3 символов\n")
                else:
                    break
        if choice == "3":
            while True:
                new = input("Придумайте ваш пароль (от 6 символов):\n")
                password = new
                if len(new) < 6:
                    print("Ваш пароль слишком короткий. Пароль должен содержать от 6 символов\n")
                else:
                    break
        else:
            new = input("Замените на новый/ое: \n")
        data.insert(int(choice), new)

        # Удаление и запись нового списка пользователей
        i = accounts.index(userData[1])
        while i in range(accounts.index(userData[0]), accounts.index(userData[5])):
            accounts.remove(accounts[i])
        accounts.remove(userData[0])
        accounts.remove(userData[5])

        with open("data\data.txt", "w") as file:
            file.write(' ' + ' '.join(accounts))
            file.close()

        #Запись редактирования акка
        with open("userData.txt", "w") as file:
            file.write(' '.join(data) + ' ')
            file.close()
        with open("data\data.txt", "a") as file:
            file.write(' '+' '.join(data))
            file.close()

        print("Теперь ваш/е/а "+ title[int(choice)-1] + ": " + new)
        break