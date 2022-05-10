age = 40
point_card = True
count = 3

if age <= 18:
    print('チケットを売ることはできません')
elif (age >= 60) or (point_card and count >= 5):
    print('チケットは1000円です')
else:
    print('チケットは1800円です')
