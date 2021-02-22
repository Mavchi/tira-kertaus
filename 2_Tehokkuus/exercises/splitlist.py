"""Annettuna on lista kokonaislukuja, ja tehtäväsi on laskea, monellako tavalla voit 
halkaista listan kahteen osaan niin, että jokainen vasemman osan alkio on pienempi 
kuin jokainen oikean osan alkio.

Esimerkiksi listassa[2, 1, 2, 5, 7, 6, 9] tapoja on 3:
[2, 1, 2] ja [5, 7, 6, 9]
[2, 1, 2, 5] ja [7, 6, 9]
[2, 1, 2, 5, 7, 6] ja [9]
Voit olettaa, että jokainen luku on välillä 1…10^9 ja listalla on enintään 10^5 lukua."""


def count(t):
    biggest_left = [0 for i in range(len(t))]
    smallest_right = [0 for i in range(len(t))]

    biggest_left[0] = t[0]
    for i in range(1, len(t)):
        if biggest_left[i-1] < t[i]:
            biggest_left[i] = t[i]
        else:
            biggest_left[i] = biggest_left[i-1]
            
    smallest_right[-1] = t[-1]
    for i in range(len(t)-2, -1, -1):
        if smallest_right[i+1] < t[i]:
            smallest_right[i] = smallest_right[i+1]
        else:
            smallest_right[i] = t[i]
        
    count = 0
    for i in range(0,len(t)-1):
        if biggest_left[i] < smallest_right[i+1]:
            count += 1
    return count


if __name__ == "__main__":
    print(count([1, 2, 3, 4, 5]))  # 4
    print(count([5, 4, 3, 2, 1]))  # 0
    print(count([2, 1, 2, 5, 7, 6, 9]))  # 3
