f = open("data\data.txt")
dataBases = f.read()
accounts = dataBases.split(" ")
f.close()

f = open("userData.txt")
dataBases=f.read()
userData = dataBases.split(" ")
f.close()
data=userData.copy()

database=[]
def id():
    f = open("id_number.txt")
    data = f.read()
    f.close()
    f = open("id_number.txt", "w")
    id = int(data) + 1
    id = str(id)
    f.write(id)
    f.close()
    database.append(id)

def email():
    while True:
        new = input("Введите ваш email-адрес:\n")
        if "@" not in new:
            print("Ваш email не содержит знак '@'\nПожалуйста, попробуйте еще раз")
        elif new.split(".")[-1] not in ["ru", "com", "net", "ua", "kz"]:
            print("Ваш email не содержит доменов '.ru', '.com' и подобных\nПожалуйста, попробуйте еще раз")
        else:
            database.append(new)
            break
def nickname():
    while True:
        new = input("Придумайте свой никнейм:\n")
        if len(new) < 3:
            print("Ваш никнейм слишком короткий. Никнейм должен содержать от 3 символов\n")
        else:
            database.append(new)
            break

def password():
    while True:
        new = input("Придумайте ваш пароль (от 6 символов):\n")
        if len(new) < 6:
            print("Ваш пароль слишком короткий. Пароль должен содержать от 6 символов\n")
        else:
            database.append(new)
            break
def write_user():
    with open("userData.txt", "w") as file:
        file.write(' '.join(data) + ' ')
        file.close()
def write_data():
    with open("data\data.txt", "a") as file:
        file.write(' ' + ' '.join(data))
        file.close()

