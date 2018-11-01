from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    try:
        n = str(numStr)
    except:#numStr이 스트링이 아니면 에러 처리
        return 'Error!'
    if len(numStr) > 3000:#romans 에 M이상이 정의 되어 있지 않으므로
        return 'So Long!'
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    idx = len(numStr)
    result = 0
    second = 1

    while 1:
        first = numStr[idx-1]
        idx -= 1
        for i in romans:
            if first in i:
                first_s = i[0]
        if second > first_s:
            result -= first_s
        else:
            result += first_s
        if idx == 0:#마지막까지 검토하면 반복 탈출
            break
        second = first_s

    return str(result)

