import json
print('Hello World!')

kaas = open('steam.json')
file = json.load(kaas)
lines = kaas.readlines()
iets = 0

for i in file:
    iets += 1

print(iets)

