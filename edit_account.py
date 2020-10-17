from fuctions import *
def edit():
    print("Что из перечисленного вы хотите изменить?")
    while True:
        choice = input("1  -- email\n2 -- никнейм\n3 -- пароль\n4 -- имя\n5 -- фамилию\n")
        mas = ["1", "2", "3", "4", "5"]
        if choice not in mas:
            print("Тут не предусмотрена эта функция, попробуйте снова")
        else:
            title = ["email", "nickname", "пароль", "имя", "фамилия"]
            dell = data[int(choice)]
            if int(choice) in range(1, 4):
                while True:
                    chec = input("Введите пароль для подверждения\n")
                    if chec != data[3]:
                        print("Указан неверный пароль, в доступе отказано. Попробуйте снова")
                    else:
                        break
            print("Вы выбрали " + dell)
            data.remove(dell)
            new = 1
            if choice == "1":
                email()
                new = database[0]
            if choice == "2":
                nickname()
                new = database[0]
            if choice == "3":
                password()
                new = database[0]
            if choice in range(4, 6):
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

            # Запись редактирования акка
            write_user()
            write_data()

            print("Теперь ваш/е/а " + title[int(choice) - 1] + ": " + new)
            break

#edit()