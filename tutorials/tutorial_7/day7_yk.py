from datetime import datetime, timedelta
from math import fsum
import math
from dateutil.relativedelta import relativedelta
# 1
given_date = datetime(2022, 4, 27, 10, 00, 00)
print(given_date)

# 2
date1 = datetime(2022, 4, 27)
date2 = datetime(2047, 3, 21)
date_diff = date2-date1
print("Difference: ", date_diff)

# 3
date_now = datetime.today()
add_month = relativedelta(months=3)
date_added = date_now + add_month
print(date_added)

# 4
a_number = int(input("a number"))
y = a_number
x = 0
z = []
while y > 0:
    x = a_number % y
    if x == 0:
        z.append(int(y))
    y -= 1
print(z)
w = sum(z)
print(w)

