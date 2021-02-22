#
#Positiivinen kokonaisluku on onnenluku, jos sen numeroiden summa on jaollinen 7:llä. 
#Esimerkiksi luku 25743 on onnenluku, koska 2+5+7+4+3=21, joka on jaollinen 7:llä.
#
#Tehtäväsi on tarkastaa, onko annettu luku n onnenluku. Voit olettaa, että n on 
#kokonaisluku välillä 1…10^9.
# 
def check(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)

    if sum%7 == 0:
        return True
    return False

if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True