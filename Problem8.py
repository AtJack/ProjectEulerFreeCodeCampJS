def largestProduct(number,adjacent):
    result = 0
    liste = []
    strNumber = str(number)
    for i in range(0,len(strNumber)):
            liste.append(int(strNumber[i]))

    for y in range(0,len(liste)-adjacent):
        for x in range(0,adjacent):
            if x == 0:
                product = liste[y]
            else:
                product *= liste[y+x]
        if product > result:
            result = product

    return result

number = 731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553953697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
print(largestProduct(number,13))
