lei = input("Anna leiviskät: \n")
nau = input("Anna naulat: \n")
luo = input("Anna luodit: \n")

lei, nau, luo = float(lei), float(nau), float(luo)

luomassa = (luo*13.3)
naumassa = ((32*13.3)*nau)
leimassa = ((20*(32*13.3))*lei)

yht = (luomassa+naumassa+leimassa)

kilot = (int(yht // 1000))
grammat = (yht % 1000)

print(f"Massa nykymittojen mukaan: {kilot}kg {grammat: .2f}g")