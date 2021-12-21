num = 0
tot = 0.0
while True:
    number = input("Enter a number")
    if number == 'exit':
        break
    try :
        num1 = float(number)
    except:
        print('error message')
        continue
    num = num+1
    tot = tot + num1
print ('exit')
print (tot,num,tot/num)
#
