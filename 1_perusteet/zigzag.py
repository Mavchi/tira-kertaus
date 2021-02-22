#
#Listalle lisätään luvut 1,2,…,n, ensin luku 1 ja sitten seuraavat luvut vuorotellen 
#oikealle ja vasemmalle puolelle. Esimerkiksi kun n=5, tuloksena on lista [5,3,1,2,4].
#
#Millainen lista tulee tietyllä n:n arvolla? Voit olettaa, että 1≤n≤1000.
def create(n):
    ar = []
    for i in range(1, n+1):
        if i%2 == 0:
            ar.append(i)
        else:
            ar = [i] + ar
    return ar

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]