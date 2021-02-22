"""Annettuna on merkkijono, jossa jokainen merkki on 0 tai 1. Tehtäväsi on muuttaa osa 
biteistä vastakkaisiksi niin, että muutosten jälkeen missään kohdassa ei ole 
vierekkäin kahta samaa bittiä. Mikä on pienin määrä muutoksia?

Esimerkiksi merkkijonossa 10010001 tarvitaan vähintään kolme muutosta. Optimaalinen 
ratkaisu on muuttaa kohdissa 0, 1 ja 5 olevat bitit, jolloin tuloksena on merkkijono 
01010101.

Voit olettaa, että merkkijonon pituus on enintään 10^5."""


def calculate(s):
    # bitstring can start with either 0 or 1, lets count which one requires less changes
    count_0, count_1 = 0, 0
    for i in range(len(s)):
        if i%2 == 0:
            if s[i] != '0':
                count_0 += 1
            else:
                count_1 += 1
        else:
            if s[i] != '1':
                count_0 += 1
            else:
                count_1 += 1

    return min(count_0, count_1)


if __name__ == "__main__":
    print(calculate("1010"))  # 0
    print(calculate("1111"))  # 2
    print(calculate("10010001"))  # 3
