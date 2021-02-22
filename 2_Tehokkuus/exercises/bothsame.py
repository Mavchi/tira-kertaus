"""Tehtäväsi on laskea, monessako merkkijonon osajonossa ensimmäinen ja viimeinen merkki 
on sama. Esimerkiksi merkkijonossa ababca tällaiset osajonot ovat
a(kolmesti)
aba
ababca
abca
b(kahdesti)
bab
c
eli yhteensä 10 osajonoa.

Voit olettaa, että merkkijono muodostuu merkeistä a–z ja siinä on enintään 10^5 
merkkiä."""


def count(s):
    d = {}
    count = 0
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        count += d[c]
    return count

if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abcd"))  # 4
    print(count("ababca"))  # 10
