x = input('enter the day:')
y = input('enter the rate:')
try:
    day = float(x)
    rate = float(y)
    hour = day/24

except:
    print('Error,Please enter the numeric digit:')
    exit()
if day<=20:
    print(day*rate)
else:
    print((((hour-20)*rate)*1.5)+rate*20)
#
