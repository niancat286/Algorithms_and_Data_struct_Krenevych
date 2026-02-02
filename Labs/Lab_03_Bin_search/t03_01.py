a = 5 # 101

print(a >> 1) #10
print(a << 1) #1010

b = 6  #110

print(a & b)    #100    логічне і
print(a | b)    #111    або
print(a ^ b)    #011    xor
print(~a)   # ~x = -(x+1)   логічне заперечення



def count_once(n):
    count = 0
    one = 1

    for i in range(n.bit_length()):
        if (one << i) & n:
            count += 1

    return count

#для 5
# 101 & 001  --> true
# 101 & 010  --> false
# 101 & 100  --> true


import sys

input = sys.stdin.readline

def count_once_v2(n):       #O(logn)
    res = 0
    while n != 0:
        is_one = n & 1
        res += is_one
        n = n >> 1
    return res

if __name__ == "__main__":
    n = int(input())
    print(count_once_v2(n))