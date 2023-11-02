from datetime import datetime, timedelta

ds = 10000
mt = 1000000
sc = 1000000000

try:
    print('Введите дату рождения в форммате ДД/ММ/ГГ')
    d_r = datetime.strptime(input(), "%d/%m/%y")
except:
    print('Введите корректную дату')
    exit()

temp = timedelta(days=10000)
data_ds = d_r + temp
print("Вам исполнится 10000 дней ", data_ds.date())
temp = timedelta(minutes=1000000)
data_ds = d_r + temp
print("Вам исполнится 1000000 ", data_ds.date())
temp = timedelta(seconds=1000000000)
data_ds = d_r + temp
print("Вам исполнится 1000000000 ", data_ds.date())
