from functions import *
print(accounts)
def checking():
    while True:
        login = input("Введите ваш никнейм/эл. адрес: ")
        password = input("Введите ваш пароль: ")
        if login not in accounts:
            print("Такого эл. адрес/никнейма не существует")
        else:
            if "@" in login:
                passw = accounts.index(login) + 2
            else:
                passw = accounts.index(login) + 1
            search_pass = accounts[passw]
            if password != search_pass:
                print("Ваш эл. адрес/никнейм или пароль неверны")
            else:
                print('Вы успешно вошли в сиситему')
                id = i = accounts.index(password) - 3
                userD = []
                while i != accounts.index(password) + 3:
                    userD.append(accounts[i])
                    i += 1
                with open("userData.txt", "w") as userData:
                    userData.write(' '.join(userD) + ' ')
                    userData.close()
                break

#checking()

