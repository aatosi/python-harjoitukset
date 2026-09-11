cm = 1
tuuma = 1

while tuuma > 0:
    tuuma = float(input('Syötä tuumat (positiivinen luku): '))
    cm = float(tuuma * 2.54)
    print(f'{tuuma: .2f} tuumaa on {cm: .2f}cm')

