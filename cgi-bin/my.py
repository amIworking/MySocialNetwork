#!/usr/bin/env python3
print("Content-type: text/html")
print()
print("""<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>База данных</title>
</head>

<body>
<h1>Добавление в базу данных Стран</h1>
<form method="post" action="scripts/form1.php">
<fieldset>
<label for="id">ID:</label><br>
<input type="number" name="id" size="11"><br>
<label for="name">Name</label><br>
<input name="name" type="text" size="30"><br>
<label for="date">Date</label><br>
<input name="date" type="text" size="30"><br>
<label for="email">Email</label><br>
<input name="email" type="text" size="30"><br>
<label for="url">URL</label><br>
<input type="url" name="url" size="50"><br>
<label for="phone">Phone</label><br>
<input name="phone" type="text" size="30"><br>
<label for="age">Age</label><br>
<input name="age" type="number" size="30"><br>
<label for="color">Color</label><br>
<input name="color" type="text" size="10"><br>
<label for="city">City</label><br>
<input name="city" type="text" size="30"><br>
<label for="about">About</label><br>
<input name="about" type="text" size="30"><br>

</fieldset>
<br>
<fieldset>
<input type="submit" name="add" value="Отправить данные">
<br>
</fieldset>
</form>
</body>""")