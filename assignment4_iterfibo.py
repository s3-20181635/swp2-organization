#head
import time
def iterfibo(n):
    sum = 0
    list = [n]
    while(1):
        for i in list:
            if not(i == 1 or i == 0):
                list.append(i-1)
                list.append(i-2)
                continue
        if list[-1] ==1 or list [-1] == 0: #가장 마지막에 들어온 숫자가 1아니면 0이면 브레이크!
            break
    for j in list:
        if j ==1 :
            sum += 1
    return sum
#body
while 1:
    nbr = int(input("enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts_f = time.time() -ts
    print("%d의 피보나치 수는 %d이고 %.6f걸렸습니다" %(nbr,fibonumber,ts_f))
