'''import sys

print('身長は？'+ str(float(sys.argv[1])) )
height = float(sys.argv[1])
weight = float(sys.argv[2])'''

print('身長を入力する or Enter key押して終了')
height = input('身長(cm)? : ')

if len(height) == 0:

    ##break
    print('OK')
else:
    height = float(height)
    height *= 0.01 
    weight = float(input('体重(kg)? : '))
    BMI = weight / pow(height,2)
    print('BMI : {:.2f}'.format(BMI))


if BMI < 18.5:
    print('yassesugi')
else:
    print('OK')

