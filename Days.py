import datetime
try:
    days_to_add = int(input('Sisesta siia päevade arv: '))
except ValueError:
    print("Vale sisend, palun sisesta täisarv.")
    exit()

current_date = datetime.datetime.now()
new_date = current_date + datetime.timedelta(days = days_to_add)
print('Antud päevade pärast on: ', new_date.strftime('%Y-%m-%d %H:%M:%S'))