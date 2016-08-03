import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
d=datetime.date.today()
date=d.strftime('%d  %B  %Y')
print(date)
