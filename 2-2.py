import random
n = random.randint(1,20)
c=0

while True:
    ans = int(input('number:'))
    if ans>20 or ans<0:
        print(輸入錯誤)
        c=c+1
    else:
        if c==5:
            print('just 5 time')
            break
        elif ans>n:
            print('小一點')
            c=c+1
        elif ans<n:
            print('大一點')
            c=c+1
        else:
            print('bingo')
            c=c+1
            print('you guess'+str(c)+'次答對了')
            break
        

