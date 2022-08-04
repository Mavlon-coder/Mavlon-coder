from datetime import datetime
# import pytz
import time


bugun=datetime.now()
print (bugun.strftime('%y-%m-%d---%H:%M:%S'))
print (bugun)


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
 




tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))



b_day = time.struct_time(tm_year=1989, tm_mon=1, tm_yday=24)
print("b_day=", b_day)

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")



print('{0:_^7}'.format('hello'))
# so'zni atrofiga _ belgisini yozish

print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# yozuv orasiga o'zgaruvchi qo'shish

print('a')
print('b', end='') # '' bu izidan davom ettirish uchun
print('a', end=' ') # ' ' bu izidan prabel bilan yozish
print('b')

s = 'This is a string.'
This continues the string  #matnni davom ettirish
print(s)

