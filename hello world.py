print('Hello World!')

kaas = open('steam.json', 'r')

lines = kaas.readlines()

for i in lines:
    print(i)

