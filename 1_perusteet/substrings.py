#
#Merkkijonon osajono on mikä tahansa merkkijonon osana oleva yhtenäinen merkkijono. 
#Esimerkiksi merkkijonon abc osajonot ovat a, b, c, ab, bc ja abc.
#
#Tehtäväsi on laskea, montako erilaista osajonoa annetussa merkkijonossa on. 
#Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.

def count(s):
    substrings = set()

    # unique characters all substrings
    for c in s:
        substrings.add(c)

    for i in range(len(s)):
        for j in range(i,len(s)):
            substrings.add(s[i:j+1])

    return len(substrings)

if __name__ == "__main__":
    print(count("aaa")) # 3
    print(count("abc")) # 6
    print(count("saippuakauppias")) # 110