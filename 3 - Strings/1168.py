# URI Online Judge 1168

num_leds = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
}

N = int(input())

for n in range(N):
    entrada = input()
    leds = 0
    for i in entrada:
        leds += num_leds[i]
    print('{} leds'.format(leds))