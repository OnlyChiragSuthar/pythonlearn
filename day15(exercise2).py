import time
from datetime import datetime
timestamp = time.strftime('%H:%M:%S')
datestamp = datetime.now()

print(datestamp.strftime('%d-%m-%y'))


if '6:00:00'<=timestamp<='12:00:00' :
    print('Good Morning,Boss')

elif '12:00:1' <=timestamp<='18:00:00' :
    print('Good Evening,Boss')

else :
    print('Good Night,Boss')

    

