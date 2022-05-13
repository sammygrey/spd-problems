# Homework 2
# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

def close_sums(arr1, arr2, t):
    csum = [arr1[0],arr2[0]]
    for i in arr1:
        for j in arr2:
            if (i + j == t):
                return [i,j]
            elif (abs(t - (i+j)) < abs(t - (csum[0]+csum[1]))):
                csum = [i, j]
    return csum


a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=20

print(close_sums(a,b,t))