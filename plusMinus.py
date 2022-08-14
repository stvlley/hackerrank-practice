arr = [1, 1, 0, -1, -1]

def plusMinus(arr):
    pos = 0
    zero = 0
    neg = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            pos += 1
        else:
            neg +=1

    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))
    