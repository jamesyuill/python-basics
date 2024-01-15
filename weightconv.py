user_weight = float(input('Weight: '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == 'K':
    converted = user_weight / 0.45
    print('Weight in Lbs: ' + str(converted))
else:
    converted = user_weight * 0.45
    print('Weight in kgs ' + str(converted))