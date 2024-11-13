from MathOperation.mulOP import mulvalue
from MathOperation.divOP import divvalue
# from 'foldername'.'filename' import 'functionname'

app1 = int(input('enter the first number= '))
app2 = int(input('enter the second number= '))
op = input('which math op you want to do ?')


if op.lower() == 'mul':
    b1 = mulvalue(app1,app2)
    print(f'multiplication={b1}')
elif op.lower() == 'div':
    b2 = divvalue(app1,app2)
    print('division',b2)
else:
    print('please choose correct operation,mul,div')
