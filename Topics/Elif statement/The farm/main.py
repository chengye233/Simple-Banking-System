money = int(input())
animal = 'sheep'
cnt = 0

if money >= 6769:
    cnt = money // 6769
elif money >= 3848:
    cnt = money // 3848
    animal = 'cow'
elif money >= 1296:
    cnt = money // 1296
    animal = 'pig'
elif money >= 678:
    cnt = money // 678
    animal = 'goat'
elif money >= 23:
    cnt = money // 23
    animal = 'chicken'

if cnt == 0:
    print('None')
elif cnt == 1 or animal == 'sheep':
    print(f'{cnt} {animal}')
else:
    print(f'{cnt} {animal}s')
