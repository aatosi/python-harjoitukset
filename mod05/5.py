yritys = 0.0
correctuser = "python"
correctpassword = "rules"
user = None
password = None

while True:
    if yritys == 5:
        print('Pääsy evätty.')
        break

    yritys += 1

    user = input("Syötä käyttäjänimi: ")
    if user == correctuser:
        password = input("Syötä salasana: ")
    elif user != correctuser:
        print('Väärä käyttäjätunnus')

    if user == correctuser and password != correctpassword:
        print('Väärä salasana')
    elif user == correctuser and password == correctpassword:
        print('Tervetuloa!')
        break