def fib(n):
    if n < 0:
        return '请输入正数'
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)
message = input('请输入你的数字')
m = int(message)
if m < 0:
    print('你输入的数字有误')
else:
  print('斐波那契数列')
  for i in range(1,m+1):
      print(fib(i))