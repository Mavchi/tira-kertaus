"""Tehtäväsi on laskea, monessako merkkijonon osajonossa jokainen merkki on sama. 
Esimerkiksi merkkijonossa abbbcaa tällaiset osajonot ovat
a(kolmesti)
aa
b(kolmesti)
bb(kahdesti)
bbb
c
eli yhteensä 11 osajonoa.

Voit olettaa, että merkkijono muodostuu merkeistä a–z ja siinä on enintään 10^5 
merkkiä."""


def count(s):
    count = 0
    length = 0
    for i in range(len(s)):
        length += 1
        count += length
        if i < len(s)-1 and s[i]!=s[i+1]:
            length = 0
    return count


if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abbbcaa"))  # 11
    print(count("abcde"))  # 5

