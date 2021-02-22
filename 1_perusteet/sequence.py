#Lukujonon ensimmäinen alkio on 1. Tämän jälkeen jokainen alkio on kuvaus edellisestä 
#alkiosta. Kuvaus saadaan kertomalla vasemmalta oikealle, montako kertaa mikäkin 
#numero esiintyy luvussa peräkkäin.
#
#Luvussa 1 on yksi ykkönen, joten sen kuvaus on 11. Luvussa 11 on kaksi ykköstä, 
#joten sen kuvaus on 21. Luvussa 21 on ensin yksi kakkonen ja sitten yksi ykkönen, 
#joten sen kuvaus on 1211. Luvussa 1211 on ensin yksi ykkönen (kuvataan 11), sitten 
#yksi kakkonen (kuvataan 12) ja lopulta kaksi ykköstä (kuvataan 21), joten sen 
#kuvaus on 111221.
#
#Lukujonon ensimmäiset 6 alkiota ovat siis 1, 11, 21, 1211, 111221, 312211.
#
#Tehtäväsi on selvittää, mikä on lukujonon kohdassa n oleva alkio. Voit olettaa, 
#että n on enintään 30.
def generate(n):
    result = [1]
    for __ in range(n-1):
        temp = []
        count = 0
        for i in range(len(result)):
            count += 1
            # if second last
            if i < len(result)-1 and result[i] != result[i+1]:
                temp += [count, result[i]]
                count = 0
        temp += [count, result[-1]]
            
        result = temp

    s = ''
    for c in result:
        s += str(c)
    return s

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 11
    print(generate(3)) # 21
    print(generate(4)) # 1211
    print(generate(5)) # 111221