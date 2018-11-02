num0=eval(input('请输入一个数字:'))
if num0<=1:
    print('这不是质数')
elif num0==2:
    print('这是一个质数')
else:
    i=2
    while i<num0:
        if num0%i==0:
            print('这不是一个质数')
            break
        i=i+1
    else:
            print('这是一个质数')
